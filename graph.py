from collections import defaultdict 
from collections import deque
class Graph:
    def countingGraphs(n: int):
        #n=nodes
        #formula to find the number edges n(n-1)//2
        return 2**(n*(n-1)//2)

    def printAdjacency(n: int, m: int, edges):
        #If 'N' = 3 and edges = {{2,1}, {2,0}}.
        #So, the adjacency list of the graph is stated below.
        #0 → 2
        #1 → 2
        #2 → 0 → 1
        graph_=defaultdict(list)
        for i in range(0, m,1):
            u=edges[i][0]
            v=edges[i][1]
            graph_[u].append(v)
            graph_[v].append(u)

        adjacencyList = []
        for i in range(n):
            adj = [i] + graph_[i]
            adjacencyList.append(adj)
        return adjacencyList
    #bfs traversal 
    def bfsOfGraph(self, V: int, adj) :
        #we will create a visted array
        visted=[0]*V
        visted[0]=1
        #first node as visted
        que=[]
        que.append(0)
        bfs=[]
        while que:
            #taking the last node edge
            node=que.pop(0)
            bfs.append(node)
            #for each edge we check the link and check whether we visted or not
            for element in adj[node]:
                #check its visted or not
                if visted[element]==0:
                    visted[element]=1
                    que.append(element)
        # code here
        return bfs
    
    def dfsOfGraph(self, V, adj):
        visted=[0]*V
        ans=[]
        def dfs(node):
            ans.append(node)
            visted[node]=1
            #for each edge check the adj nodes and find the depth
            for element in adj[node]:
                if visted[element]==0:
                    
                    dfs(element)
            
        dfs(0)
        return ans
     

    def bfsOfGraph(self,v, adj,visted):
        #we will create a visted array
        visted[v]=1
        #first node as visted
        que=[]
        que.append(v)
        while que:
            #taking the last node edge
            node=que.pop(0)
            #for each edge we check the link and check whether we visted or not
            for element in adj[node]:
                #check its visted or not
                if visted[element]==0:
                    visted[element]=1
                    que.append(element)

    def findCircleNum(self, isConnected):
        adj=defaultdict(list)
        #we are creating adj list which hold the nodes link
        for i in range(0, len(isConnected[0]),1):
            for j in range(0,len(isConnected[0]),1):
                if isConnected[i][j]==1:
                        adj[i].append(j)
        visted=[0]*len(isConnected)
        #visted array
        count=0
        #for each element we check the connection
        for element in range(0,len(isConnected),1):
            #since we check the connection if there is a node linked it will be marked 
            if visted[element]==0:
                # whenever we check a missed out we add a count that will be a province
                self.bfsOfGraph(element,adj,visted)
                count+=1
        return count
    
    def orangesRotting(self, grid):
        #we need to go with the BFS ALGO since we are doing level
        # we need a que which holds the rooten orange
        #we mark it visted and mark the 4-directionally adjacent 
        n=len(grid)
        m=len(grid[0])
        que=deque()
        visted=set()
        for i in range(0,n,1):
            for j in range(0,m,1):
                if grid[i][j]==2:
                    #checking its rotten
                    #we are marking only rotton
                    que.append([i,j,0])
                elif  grid[i][j]==1:
                        visted.add((i, j))
        time=0
        while visted and que:
			# BFS iteration
            for _ in range(len(que)):
                i, j = que.popleft()  # obtain recent rotten orange
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visted:  # check if adjacent orange is fresh
                        visted.remove(coord)
                        que.append(coord)
            time += 1
        for i in range(0,n,1):
            for j in range(0,m,1):
                if grid[i][j]==1 and (i,j) not in visted:
                    return -1
        #means we have missed some 
        return -1 if visted else time
    
    def floodFill(self, image, sr: int, sc: int, color: int):
        #we need to go with the BFS ALGO since we are doing level
        # we need a que which holds the rooten orange
        #we mark it visted and mark the 4-directionally adjacent 
        n=len(image)
        m=len(image[0])
        flood=image[sr][sc]
        def dfs(i,j):
            if i>=0 and i<n and j>=0 and j<m and image[i][j]==flood and image[i][j] != color:
                image[i][j] = color
                #directions
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        dfs(sr, sc)
        return image
    
    def isCycle(self, V , adj):
            #we need to create a detect functions to avoid compoents
            #this is Bfs Intuition
            #check level by and make sure u carry the parent
            # when u go level but a node is reached before u and u didn't come from that node(not a parent)
            #that makes a cycle
            visted=[0]*V
            def detect_cycle(src,adj,visted):
                visted[src]=1
                que=deque()
                que.append((src,-1))
                while que:
                    node,parent=que.popleft()
                    for element in adj[node]:
                        if visted[element]==0:
                            visted[element]=1
                            que.append((element,node))
                        #main condition of cycle
                        elif parent!=element:
                            return True
            for i in range(0,V,1):
                if visted[i]!=1:
                    if(detect_cycle(i,adj,visted)):
                        return 1
                        
            return 0

    def isCyclic(self, V, adj):
        # since its directed graph we follow a dfs
        #we track visted and path visted 
        #whenever we are unable to find a path we unmark pathvisted 
        #when a node is marked and path visted is not marked it means its a dfs
        def detect_cycle(node,adj,visted,pathvisted):
            visted[node]=1
            pathvisted[node]=1
            
            for element in adj[node]:
                if visted[element]!=1:
                    if detect_cycle(element,adj,visted,pathvisted)==True:
                        return True
                elif pathvisted[element]==1:
                    return True
        
            pathvisted[node]=0
            return False
        
        pathvisted=[0]*V
        visted=[0]*V
        for i in range(0,V,1):
            if visted[i]==0:
                if detect_cycle(i,adj,visted,pathvisted)==True:
                        return 1
                        
        return 0
    def updateMatrix(self, mat):
        #BFS traversal METHOD 
        #WITH CORD AND DISTANCE PARAM
        n=len(mat)
        m=len(mat[0])
        min_=0
        que=deque()
        visted=set()
        dist_=[[0 for x in range(n)] for y in range (m)]
        # for i in range(0,n,1):
        #     temp=[]
        #     for j in range(0,m,1):
        #         temp.append(0)
        #     dist_.append(temp)
        for i in range(0,n,1):
            for j in range(0,m,1):
                if mat[i][j]==0:
                    que.append((i,j,0))
                    visted.add((i,j))
        while que:
            i,j,dist=que.popleft()
            dist_[i][j]=dist
            for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord not in visted and coord[0]>=0 and coord[0]<n and coord[1]>=0 and coord[1]<m:
                        visted.add(coord)
                        que.append((coord[0],coord[1],dist+1))

        return dist_
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        result = [row[:] for row in mat]
        visited = set()
        queue = deque()

        # Find all 0s and add them to the queue with distance 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    visited.add((i, j))
                    queue.append((i, j, 0))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        # Perform BFS to update distances
        while queue:
            row, col, steps = queue.popleft()

            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc

                if 0 <= next_row < m and 0 <= next_col < n and (next_row, next_col) not in visited:
                    result[next_row][next_col] = steps + 1
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return result

    def solve(self, mat):
        #if its O in the border and linked with the internal blocks it won't be covered with the 'X'
        # in that case we need to find the full link
        # for other O we can mark it as X
        #DFS approach
        n=len(mat)
        m=len(mat[0])
        print(m,n)
        visted=[row[:] for row in mat]
        delrow=[-1, 0, +1, 0]
        delcol=[0, 1, 0, -1]
        def dfs(i,j,mat,visted):
            visted[i][j]=1
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for k in range (0,4,1):
                nrow = i + delrow[k]
                ncol = j + delcol[k]
                if(nrow >=0 and nrow <n and ncol >= 0 and  ncol < m 
                and visted[nrow][ncol]!=1 and  mat[nrow][ncol] == 'O'):
                    dfs(nrow, ncol,mat,visted)
        #first row
        for j in range(0,m,1):
            if visted[0][j]!=1 and mat[0][j]=='O':
                    dfs(0,j,mat,visted)
        #last row
        for j in range(0,m,1):
            if visted[n-1][j]!=1 and mat[n-1][j]=='O':
                    dfs(n-1,j,mat,visted)
        #first col
        for i in range(0,n,1):
            if visted[i][0]!=1 and mat[i][0]=='O':
                    dfs(i,0,mat,visted)

        for i in range(0,n,1):
            if visted[i][m-1]!=1 and mat[i][m-1]=='O':
                    dfs(i,m-1,mat,visted)
                          
        for i in range(0,n,1):
            for j in range(0,m,1):
                if mat[i][j]=='O' and visted[i][j]!=1:
                    visted[i][j]=1
                    mat[i][j]='X'


        return mat



 
g=Graph()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
ans=g.solve(board)
print(ans)