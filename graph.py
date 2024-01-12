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
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
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


    
                
    
g=Graph()
grid = [[2,1,1],[1,1,0],[0,1,1]]
ans=g.orangesRotting(grid)
print(ans)