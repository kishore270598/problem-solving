from collections import defaultdict 
from collections import deque
from string import ascii_lowercase
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
    def numEnclaves(self, grid):
        n=len(grid)
        m=len(grid[0])
        visted=[[0 for x in range(m)] for y in range (n)]
        delrow=[-1, 0, +1, 0]
        delcol=[0, 1, 0, -1]
        def dfs(i,j,visted):
            visted[i][j]=1
            for k in range(0,4,1):
                nrow=i+delrow[k]
                ncol=j+delcol[k]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and visted[nrow][ncol]!=1 and grid[nrow][ncol]==1:
                    dfs(nrow,ncol,visted)

        #first col
        for i in range(0,n,1):
            if grid[i][0]==1 and visted[i][0]!=1:
                dfs(i,0,visted)
        #last col
        for i in range(0,n,1):
            if grid[i][m-1]==1 and visted[i][m-1]!=1:
                dfs(i,m-1,visted)

        #firstrow 
        for i in range(0,m,1):
            if grid[0][i]==1 and visted[0][i]!=1:
                dfs(0,i,visted)
        #lastrow
        for i in range(0,m,1):
            if grid[n-1][i]==1 and visted[n-1][i]!=1:
                dfs(n-1,i,visted)
        c=0
        print(visted)
        for i in range(0,n,1):
            for j in range(0,m,1):
                if grid[i][j]==1 and visted[i][j]!=1:
                        c+=1

        return c

    def ladderLength(self, beginWord, endWord, wordList):
        #we do with BFS traversal
        #for every word we take a loop and try to change it each character 
        #make sure its there in the wordlist
        #once we meet it we remove it from wordlist
        deq =deque()
        bank = set(wordList)
        deq.append(beginWord)
        count = 0
        n = len(beginWord)
        while deq:
            for _ in range(len(deq)):
                cur_word = deq.popleft()
                if cur_word == endWord:
                    return count + 1
                for i in range(n):
                    #Hit---#hot
                    for ch in [chr(ord('a') + k) for k in range(26)]:
                        new_word = cur_word[:i]+ch+cur_word[i + 1:]
                        if new_word in bank:
                            deq.append(new_word)
                            bank.discard(new_word)
        return 0
    ################################
    #Word 2 problem very important #
    ################################
    def findLadders(self, beginWord, endWord, wordList):
        #using the words we form a pattern
        # for example lets take HIT -- > we store all the patterns for that word
        # HIT---> H_T,_IT,HI_


        wordList.append(beginWord)
        nei = collections.defaultdict(list)
        #Creating adjs  list using pattern over the words
        for w in wordList :
            for k in range(len(w)) :
                pattern = w[:k] + '-' + w[k + 1:]
                nei[pattern].append(w)
        q = collections.deque([(beginWord, [beginWord])])
        #This format is to save the last word of the seque (beginWord,...)
        vis = set([beginWord])
        res = []
        
        while q :
            auxSet = set() #this enable have control over the graph paths. The key for this problem
            
            for s in range(len(q)) :
                w, seq = q.popleft()
                if w == endWord :
                    res.append(seq)      
                    
                for k in range(len(w)) : #sech adjs list 
                    pattern = w[:k] + '-' + w[k + 1:]
                    for adj in nei[pattern] :# all the possible pattern for that word we are adding 
                        if adj not in vis :                        
                            auxSet.add(adj)
                            q.append((adj, seq[:]+[adj]))
        
            vis.update(auxSet) #this fun will update set

        return res

    def findLadders(self, beginWord,endWord ,wordList):
        # 1. Create adjacency list
        def adjacencyList():
            # Initialize the adjacency list
            adj = defaultdict(list)
            # Iterate through all words
            for word in wordList:
                # Iterate through all characters in a word
                for i, _ in enumerate(word):
                    # Create the pattern
                    pattern = word[:i] + "*" + word[i + 1 :]
                    # Add a word into the adjacency list based on its pattern
                    adj[pattern].append(word)
            return adj
        # 2. Create reversed adjacency list
        def bfs(adj):
            # Initialize the reversed adjacency list
            reversedAdj = defaultdict(list)
            # Initialize the queue
            queue = deque([beginWord])
            # Initialize a set to keep track of used words at previous level
            visited = set([beginWord])
            while queue:
                # Initialize a set to keep track of used words at the current level
                visitedCurrentLevel = set()
                # Get the number of words at this level
                n = len(queue)
                # Iterate through all words
                for _ in range(n):
                    # Pop a word from the front of the queue
                    word = queue.popleft()
                    # Generate pattern based on the current word
                    for i, _ in enumerate(word):
                        pattern = word[:i] + "*" + word[i + 1 :]
                        # Itereate through all next words
                        for nextWord in adj[pattern]:
                            # If the next word hasn't been used in previous levels
                            if nextWord not in visited:
                                # Add such word to the reversed adjacency list
                                reversedAdj[nextWord].append(word)
                                # If the next word hasn't been used in the current level
                                if nextWord not in visitedCurrentLevel:
                                    # Add such word to the queue
                                    queue.append(nextWord)
                                    # Mark such word as visited
                                    visitedCurrentLevel.add(nextWord)
                # Once we done with a level, add all words visited at this level to the visited set
                visited.update(visitedCurrentLevel)
                # If we visited the endWord, end the search
                if endWord in visited:
                    break
            return reversedAdj
        # 3. Construct paths based on the reversed adjacency list using DFS
        def dfs(reversedAdj, res, path):
            # If the first word in a path is beginWord, we have succesfully constructed a path
            if path[0] == beginWord:
                # Add such path to the result
                res.append(list(path))
                return res
            # Else, get the first word in a path
            word = path[0]
            # Find next words using the reversed adjacency list
            for nextWord in reversedAdj[word]:
                # Add such next word to the path
                path.appendleft(nextWord)
                # Recursively go to the next word
                dfs(reversedAdj, res, path)
                # Remove such next word from the path
                path.popleft()
            # Return the result
            return res
        # Do all three steps
        adj = adjacencyList()
        reversedAdj = bfs(adj)
        res = dfs(reversedAdj, [], deque([endWord]))
        return res
    def numIslands(self,grid):
        n=len(grid)
        m=len(grid[0])
        visted=[]
        for i in range(0,n,1):
            z=[]
            for j in range(0,m,1):
                z.append(0)
            visted.append(z)
                
        count=0
        def find_island(row,col,visted):
            visted[row][col] = 1
            for k in range(-1,2,1):
                for l in range(-1,2,1):
                    nrow = row + k
                    ncol = col + l
                    if  nrow>=0 and ncol>=0 and nrow<n and ncol<m and visted[nrow][ncol]!=1 and grid[nrow][ncol]==1:
                        visted[nrow][ncol]=1
                        find_island(nrow,ncol,visted)
                            
        for i in range(0,n,1):
            for j in range(0,m,1):
                if visted[i][j]!=1 and grid[i][j]==1:
                    count+=1
                    find_island(i,j,visted)
        return count

    def isBipartite(self, graph):
        #when a graph length is node is odd we can't divide it 
        n=len(graph)
        def dfs(node,col,color,graph):
            color[node]=col
            for element in graph[node]:
                if color[element]==-1:
                    if col==0:
                        if dfs(element,1,color,graph)==False:
                            return False
                    else:
                        dfs(element,0,color,graph)
                elif color[element]==col:
                    #its adj col so it can't be bipartite
                    return False
    
        # we create a coloured array as visted array to different the 0/1 
        color=[-1]*n
        #for components
        for i in range(0,n,1):
            if color[i]==-1:
                if (dfs(i,0,color,graph))==False:
                    return False
        return True
    #Topo Sort
    def topoSort(self, V, adj):
        visted=[0]*V
        stack=[]
        def dfs(node,visted,adj,stack):
            visted[node]=1
            for element in adj[node]:
                if visted[element]!=1:
                    dfs(element,visted,adj,stack)
            stack.append(node)
        for i in range(0,V,1):
            if visted[i]!=1:
                dfs(i,visted,adj,stack)
        ans=[]
        while stack:
            ans.append(stack.pop())
            
        return ans 
    #TOPOLOGICAL STACK (DFS) WITHOUT INDEGRE**************************
    def findOrder(self, V, adj):
        visted=[0]*V
        stack=[]
        n=len(adj)
        print(n)
        graph=defaultdict(list)
        for node,pre in adj:
            graph[node].append(pre)

        def dfs(node,visted,adj,stack):
            visted[node]=0
            for element in graph[node]:
                if visted[element]!=1:
                    dfs(element,visted,graph,stack)
            stack.append(node)
        for i in range(0,V,1):
            if visted[i]!=1:
                dfs(i,visted,graph,stack)
        ans=[]
        while stack:
            ans.append(stack.pop())
            
        return ans 
    #TOPOLOGICAL QUE (BFS) WITH INDEGRE**************************
    def findOrder(self, V, adj):
        #Kahn's Algorithm
        #find the total indegree (node coming inside the our main node)
        #whenever we find the less degre we add in stack and 
        graph=defaultdict(list)
        in_deg=defaultdict(int)
        for after, before in adj:
            graph[before].append(after)
            in_deg[after] += 1
        #which means we added a zero guy
        que=deque()
        for i in range(V):
            if in_deg[i]==0:
                que.append(i)
        topo=[]

        while que:
            node=que.popleft()
            topo.append(node)
            for element in graph[node]:
                in_deg[element]-=1
                if in_deg[element]==0:
                    que.append(element)
        return topo if len(topo) == V else []

 
g=Graph()
board = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
numCourses = 2
prerequisites = [[1,0]]
ans=g.findOrder(numCourses,prerequisites)
print(ans)