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
    

    #Course Schedule
    def canFinish(self, numCourses, prerequisites):
        in_degre=defaultdict(int)
        adj=defaultdict(list)
        z=[]
        for after,before in prerequisites:
            adj[before].append(after)
            in_degre[after]+=1
        que=deque()
        for i in range(numCourses):
            if in_degre[i]==0:
                que.append(i)
        while que:
            node=que.popleft()
            z.append(node)
            for element in adj[node]:
                in_degre[element]-=1
                if in_degre[element]==0:
                    que.append(element)
        if len(z)==numCourses:
            return True
        else:
            return False
    #Course Schedule 2    
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
    
        






    def eventualSafeNodes(self, adj):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        #same as cyclic dectection where a node is a part of cyclic then it can't be terminal
        #so we will do a marked check and run a loop for nodes
        #and if checks where still 1  then its terminal
        V=len(adj)
        def detect_cycle(node,adj,visted,pathvisted,checks):
            visted[node]=1
            pathvisted[node]=1
            checks[node]=0
            for element in adj[node]:
                if visted[element]!=1:
                    if detect_cycle(element,adj,visted,pathvisted,checks)==True:
                        checks[node]=0
                        return True
                elif pathvisted[element]==1:
                    checks[node]=0
                    return True
            checks[node]=1
            pathvisted[node]=0
            return False
        
        pathvisted=[0]*V
        visted=[0]*V
        ans=[]
        checks=[0]*V
        for i in range(0,V,1):
            if visted[i]==0:
                detect_cycle(i,adj,visted,pathvisted,checks)
        for i in range(V):
            if (checks[i]==1):
                ans.append(i)
        return ans
    #alien ques
    def findOrder(self,alien_dict, N, K):
            def topoSort(V, adj):
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
            adj=defaultdict(list)
            topo=[]
            for i in range(0,len(alien_dict)-1,1):
                s1=alien_dict[i]
                s2=alien_dict[i+1]
                min_len=min(len(s1),len(s2))
                for j in range(min_len):
                    if s1[j] != s2[j]:
                        adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                        break
            topo=topoSort(K,adj)
            z = ''.join(chr(node + ord('a')) for node in topo)
            return z
    def shortestPath(self, edges, n, m, src):
        que=deque()
        adj=defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        que.append(src)
        dist=[float('inf')]*n
        dist[src] = 0
        while que:
            node=que.popleft()
            for element in adj[node]:
                #which checks the distance is shorted and updated the correct path
                if dist[node]+1<dist[element]:
                    dist[element] = 1 + dist[node]
                    que.append(element)
        
        for i in range(n):
           if dist[i] == float('inf'):
               dist[i] = -1
        return dist# code he
    
    def shortestPath(self, n, m, edges): #dag 
        graph=defaultdict(list)
        que=deque()
        distance=[float('inf')]*n
        for i,j,k in edges:
            graph[i].append((j,k))
        que.append(0)
        distance[0]=0
        while que:
            node=que.popleft()
            for element,dis in graph[node]:
                if distance[node]+dis<distance[element]:
                    distance[element] = dis + distance[node]
                    que.append(element)
        for i in range(n):
            if distance[i] == float('inf'):
                distance[i]=-1
        return distance
    
    def dijkstra(self, V, adj, S):
         #code here
        import heapq
        g = defaultdict(list)
        for i in range(len(adj)):
            for u, w in adj[i]:
                g[i].append([u,w])
                g[u].append([i,w])
        q = [(0, S)]
        dist = [float('inf')]*V
        dist[S] = 0
        #since its pop reverse
        while q:
            dis, top = heapq.heappop(q)
            for adjNode, weight in g[top]:
                #it means we see that current node has more value so make sure we set a less value
                if dist[adjNode] > weight + dis:
                    dist[adjNode] = weight + dis
                    heapq.heappush(q, (weight + dis, adjNode))
        return dist
    
    def shortestDistance(self,N,M,A,X,Y):
        dist=[[float('inf')]*M for _ in range(N)]
        dist[0][0]=0
        q=deque()
        q.append((0,(0,0)))
        del_row=[-1,0,1,0]
        del_col=[0,1,0,-1]
        if A[0][0]==0: return -1
        if X==0 and Y==0 : return 0
        
        while q:
            dst,curr=q.popleft()
            row=curr[0]
            col=curr[1]
            for i in range(4):
                nrow = row + del_row[i]
                ncol = col + del_col[i]
                
                if nrow >= 0 and N > nrow and ncol >=0  and ncol < M and A[nrow][ncol]==1 and dst+1<dist[nrow][ncol]:
                    dist[nrow][ncol]=dst+1
                    if nrow==X and ncol==Y:
                        return dst+1
                        
                    q.append((dst+1,(nrow,ncol)))    
                    
        return -1            
        #code here
    
    #Path With Minimum Effort
    def minimumEffortPath(self, heights):
        from heapq import heappush, heappop
        N=len(heights)-1
        M=len(heights[0])-1
        q=[(0,(0,0))]
        del_row=[-1,0,1,0]
        del_col=[0,1,0,-1]
        costSoFar = {(0,0): 0} #we can store the x,y their cost
        min_=0
        trgt=(N,M)
        import math
        while q:
            distance,node=heappop(q)
            row,col=node
            if node == trgt: # - Dikstra can have early terminate
                break
            for i in range(4):
                nrow = row + del_row[i]
                ncol = col + del_col[i]
                if nrow >= 0 and nrow <=N and ncol >= 0 and ncol <=M:
                    edgeCost = max(distance, abs(heights[row][col] - heights[nrow][ncol]))
                    if (nrow,ncol) not in costSoFar or ( (nrow,ncol) in costSoFar and costSoFar[(nrow,ncol)]>edgeCost):
                        costSoFar[(nrow,ncol)]=edgeCost
                        heappush(q, (edgeCost, (nrow, ncol)))
        return costSoFar[trgt]
    #Cheapest Flights Within K Stops
    def findCheapestPrice(self, n, flights, src, dst, k):
        # [soruce stops,start,end]
        q=deque()
        q.append([0,(src,0)])
        graph=defaultdict(list)
        distance=[float('inf')]*n
        distance[src]=0
        for u, v, w in flights:
            graph[u].append((v, w))
        while q:
            stops,(node,cost)=q.popleft()
            if stops>k:
                continue
            for element,edw in graph[node]:
                if cost+edw<distance[element] and stops<=k:
                    distance[element]=cost+edw
                    q.append((stops+1,(element,cost+edw)))
        
        if distance[dst]==float('inf'):
            return -1
        else:
            return distance[dst]
    #networkDelayTime 
    def networkDelayTime(self, times, n, k):
        graph=defaultdict(list)
        from heapq import heappush, heappop
        for u, v, w in times:
            graph[u].append((v, w))
        distance=[float('inf')]*n
        q=[(0,k)]
        distance[k-1]=0
        visited=set()
        while q:
            dist,node=heappop(q)
            visited.add(node)
            if len(visited)==n:
                return dist
            for element,edw in graph[node]:
                if element not in visited:
                    heapq.heappush(q, (dist+edw, element))

        return -1
    def minimumMultiplications(self, arr, start, end ):
        # code here
        que=deque()
        distance=[float('inf')]*100000
        distance[start]=0
        que.append((start,0))
        if start==end:
            return 0
        while que:
            node,step=que.popleft()
            for element in arr:
                num=(element*node)%100000
                if (step+1<distance[num]):
                    distance[num]=step+1
                    if num==end:
                        return step+1
                    que.append((num,step+1))
                    
                    

        return -1

    def bellman_ford(self, V, edges, S):
        ans=[10**8 for i in range(V)]
        ans[S]=0
        for it in range(0,V-1):
            for i,j,w in edges:
                if ans[i]!=10**8 and ans[i]+w<ans[j]:
                    ans[j]=ans[i]+w
        
        x=[i for i in ans]
        # print(ans)
        for i,j,w in edges:
            if x[i]!=10**8 and x[i]+w<x[j]:
                x[j]=x[i]+w
        if x==ans:
            return ans
        return [-1]
    #MST PRIMS ALGO
    def spanningTree(self, V, adj):
        from heapq import heappush,heappop
        #[weight,node]
        q=[]
        q.append([0,0])
        visted=[0]*V
        sum_=0
        while q:
            weight,node=heappop(q)
            if(visted[node]==1):
                continue
            visted[node]=1
            sum_+=weight
            for s,w in adj[node]:
                if visted[s]!=1:
                    heappush(q,(w,s))
        return sum_
class Disjoint:
    def __init__(self,n):
        self.size=[1]*n #union by size
        #self.rank=[0]*n
        self.parent=[0]*n
        for i in range(n):
            self.parent[i]=i
    
    def find_parent(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self,u,v):
        ultimate_u=self.find_parent(u)
        ultimate_v=self.find_parent(v)
        if (ultimate_u==ultimate_v):
            return
        # if self.rank[ultimate_u]<self.rank[ultimate_v]:
        #     self.parent[ultimate_u]=ultimate_v
        
        # elif self.rank[ultimate_v]<self.rank[ultimate_u]:
        #     self.parent[ultimate_v]=ultimate_u
        # else:
        #     self.parent[ultimate_v]=ultimate_u
        #     self.rank[ultimate_u]+=1
        if self.size[ultimate_u]<self.size[ultimate_v]:
            self.parent[ultimate_u]=ultimate_v
            self.size[ultimate_v]+=self.size[ultimate_u]
        else:
            self.parent[ultimate_v]=ultimate_u
            self.size[ultimate_u]+=self.size[ultimate_v]
    def main(self):
        # Example usage
        size = 7
        ds = Disjoint(size)
        # Perform some union operations
        ds.union_by_rank(0, 1)
        ds.union_by_rank(1, 2)
        ds.union_by_rank(3, 4)
        ds.union_by_rank(5, 6)
        ds.union_by_rank(4, 5)
        if ds.find_parent(2)==ds.find_parent(6):
            print('yes')
        else:
            print('no')
        ds.union_by_rank(2, 6)
        if ds.find_parent(2)==ds.find_parent(6):
            print('yes')
        # Find the representative of each element

#class Solution:
    def spanningTree(self, V, adj):
        edges=[]
        for i in range(V):
            for it in adj[i]:
                edges.append([it[1],it[0],i])
        edges.sort()
        mstwt=0
        ds=Disjoint(V)
        for i in edges:
            wt=i[0]
            u=i[1]
            v=i[2]
            if ds.find_parent(u)!=ds.find_parent(v):
                mstwt+=wt
                ds.union_by_rank(u,v)
        return mstwt


    def makeConnected(self, n, connections):
        #since mst required nodes--- edges(n-1)
        #if extra that need to be added to the compenet -1== extra nodes
        d=Disjoint(n)
        edges_req=n
        #this means required edges_requied for mst
        for u,v in connections:
            #mst required for edges
            edges_req-=d.union_by_rank(u,v)
        if edges_req - d.duplicates <= 1:
            #checking node=edges-1
            #---> checking above nodes-deges<=1 
            return edges_req-1
        else:
            return -1
    
    def removeStones(self, stones):
        #intuition if we take the node as row and col as a node
        #number componet (number node)-number compoent 
        max_row=0
        max_col=0
        n=len(stones)
        for i in stones:
            max_row=max(max_row,i[0])
            max_col=max(max_col,i[1])
            #this to find the last element in row take it as node and from there we follow
            #col as node ..
        unique_nodes = set()
        max_row+=1
        max_col+=1
        d=Disjoint(max_row+max_col)
        for i in stones:
            r=i[0]
            c=i[1]+max_row
            d.union_by_rank(r,c)
            unique_nodes.add(r)
            unique_nodes.add(c)
        c=0
        for item in unique_nodes:
            if item==d.find_parent(item):
                c+=1
        return n-c

    def accountsMerge(self, accounts):
        maps=dict()
        ds=Disjoint(len(accounts))
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i]),1):
                string_mail=accounts[i][j]
                if string_mail not in maps:
                    maps[string_mail]=i
                else:
                    ds.union_by_rank(i,maps[string_mail])
        
        merged_mail = [[]for _ in range(n)]
        
        for mail, node in maps.items():
            # we need to merge it with the node that means the parent one
            # so we check the ultimate parent
            up = ds.find_parent(node)
            merged_mail[up].append(mail)
            
        
        ans = []
        for i in range(n):
            # since we negalted we removed it
            if not merged_mail[i]:
                continue
            # we sort the emails
            merged_mail[i].sort()
            #the first name and the list
            temp = [accounts[i][0]]  + merged_mail[i]
            ans.append(temp)
        return ans
    
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        ds=Disjoint(rows*cols)
        visted=[]
        for i in range(rows):
            temp=[]
            for j in range(cols):
                temp.append(0)
            visted.append(temp)
        ans=[]
        #there is changes on island that should be tracked so for that ans list
        count=0
        for element in operators:
            row=element[0]
            col=element[1]
            if visted[row][col]==1:
                ans.append(count)
                continue
            visted[row][col]=1
            count+=1
            dr=[0,-1,0,1]
            dc=[-1,0,1,0]
            for i in range(4):
                new_r=dr[i]+row
                new_c=dc[i]+col
                #check the validity
                if (new_r<rows and new_c<cols and new_r>=0 and new_c>=0):
                    if visted[new_r][new_c]==1:
                        #check if its already connected
                        node=row*cols+col
                        adjnode=new_r*cols+new_c
                        if(ds.find_parent(node)!=ds.find_parent(adjnode)):
                            count-=1
                            #means the island is connected
                            ds.union_by_rank(node,adjnode)
            ans.append(count)
        return ans
    def largestIsland(self, grid):
        n = len(grid)
        ds = Disjoint(n * n)
        # first step is connecting the components
        delrow = [1, 0, -1, 0]
        delcol = [0, 1, 0, -1]
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                for ind in range(4):
                    nrow = row + delrow[ind]
                    ncol = col + delcol[ind]
                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < n and grid[nrow][ncol] == 1:
                            nodeNo = row * n + col
                            adjNodeNo = nrow * n + ncol
                            ds.union_by_rank(nodeNo, adjNodeNo)
        
        # making 0 -> 1
        sizeOflargestIsland = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                # storing componenets
                setOfComponenents = set()
                for ind in range(4):
                    nrow = row + delrow[ind]
                    ncol = col + delcol[ind]
                    if nrow >= 0 and nrow < n and ncol >= 0 and ncol < n \
                        and grid[nrow][ncol] == 1:
                            adjNodeNo = nrow * n + ncol
                            setOfComponenents.add(ds.find_parent(adjNodeNo))
                
                sizeOfIsland = 0
                for it in setOfComponenents:
                    sizeOfIsland += ds.size[it]
                sizeOflargestIsland = max(sizeOfIsland + 1, sizeOflargestIsland)
        #what if there all the 1 that is the case we need to take the max of all the size of parent that means
        #everything will be connected 
        sizeOflargestIsland = max(sizeOflargestIsland, ds.size[ds.find_parent(n*n-1)])

        return sizeOflargestIsland
        # code hered.un
    


    def swimInWater(self, grid):
        #we use dijistra algo
        from heapq import heappush, heappop
        n=len(grid)
        min_heap=[[grid[0][0],0,0]] #(time/heigh,r,c)
        visted=set()
        visted.add((0,0))
        directions=[[0,-1],[0,1],[-1,0],[1,0]]
        ans=0
        while min_heap:
            time,i,j=heapq.heappop(min_heap)
            ans=max(time,ans)
            if i==n-1 and j==n-1:
                return ans
            for x, y in directions:
                if(0<=i+x<n and 0<=j+y<n and (i+x, j+y) not in visted):
                    visted.add((i+x, j+y))
                    heappush(min_heap,[grid[i+x][j+y],i+x, j+y])
    
    
    #Using Tarjan’s Algorithm of time in and low time:
    def criticalConnections(self, n, connections):
        graph=defaultdict(set)
        for x,y in connections:
            graph[x].add(y)
            graph[y].add(x)
    
        def bridgeUtil(u, visited, parent, low, disc, time): 

            # Mark the current node as visited and print it 
            visited[u]= True

            # Initialize discovery time and low value 
            disc[u] = time[0]
            low[u] = time[0]
            time[0]+=1

            #Recur for all the vertices adjacent to this vertex 
            ans=[]
            for v in graph[u]: 
                # If v is not visited yet, then make it a child of u 
                # in DFS tree and recur for it 
                if visited[v] == False : 
                    parent[v] = u 
                    find = bridgeUtil(v, visited, parent, low, disc,time) 
                    ans.extend(find)

                    # Check if the subtree rooted with v has a connection to 
                    # one of the ancestors of u 
                    low[u] = min(low[u], low[v]) 


                    ''' If the lowest vertex reachable from subtree 
                    under v is below u in DFS tree, then u-v is 
                    a bridge'''
                    if low[v] > disc[u]: 
                        ans.append([u,v])


                elif v != parent[u]: # Update low value of u for parent function calls. 
                    low[u] = min(low[u], disc[v]) 
        return ans
    
    def kosaraju(self, V, adj):
        def dfs(n):
            vis1.add(n)
            for i in adj[n]:
                if i not in vis1:
                    dfs(i)
            q.append(n)


        #step 1 dfs: sorting by finishing time
        q=[]            
        vis1=set()
        for i in range(V):
            if i not in vis1:
                dfs(i)


        # step 2: rev all edges       
        revadj=[[] for i in range(V)]
        for n in range(V):
            for a in adj[n]:
                revadj[a].append(n)
        
        # for stp3 
        def revdfs(n):
            vis2.add(n)
            for i in revadj[n]:
                if i not in vis2:
                    revdfs(i)


        #step 3: final dfs to cnt scc
        vis2=set()
        cnt=0
        while q:
            i=q.pop()
            if i not in vis2:
                revdfs(i)
                cnt+=1


        return cnt

    def articulationPoints(self, V, adj):
        visted=[0]*V
        mark=[0]*V
        disc = [float("Inf")] * (V) 
        low = [float("Inf")] * (V) 
        ans=[]
        time=[0]
        def dfs(node,parent,visted,disc,low,mark,time,adj):
            visted[node]=1
            low[node]=time[0]
            disc[node]=time[0]
            time[0]+=1
            child=0
            for adjnode in adj[node]:
                if adjnode==parent:
                    continue
                if visted[adjnode]!=1:
                    dfs(adjnode,node,visted,disc,low,mark,time,adj)
                    #once dfs is completed take the low
                    low[node]=min(low[node],low[adjnode])
                    if low[adjnode]>=disc[node] and parent!=-1:
                        mark[node]=1
                    child+=1
                else:
                    #i will take the low of time of insertion of the visted guy
                    #since we break the point it won't able to reach
                    low[node]=min(low[node],disc[adjnode])
            
            if child>1 and parent==-1:
                mark[node]=1
        
        
        for i in range(V):
            if visted[i]!=1:
                dfs(i,-1,visted,disc,low,mark,time,adj)
        ans = []
        for i in range(V):
            if mark[i] ==1:
              ans.append(i)
        return ans if len(ans) else [-1]
                

d=Disjoint(7)
d.main()






























g=Graph()
board = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
numCourses = 2
prerequisites = [[1,0]]
heights =[[1,2,2],[3,8,2],[5,3,5]]
ans=g.minimumEffortPath(heights)
print(ans)