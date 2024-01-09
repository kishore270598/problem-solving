from collections import defaultdict 
class Graph:
    def countingGraphs(n: int):
        #n=nodes
        #formula to find the number edges n(n-1)//2
        return 2**(n*(n-1)//2)

    def printAdjacency(n: int, m: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
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
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
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

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
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