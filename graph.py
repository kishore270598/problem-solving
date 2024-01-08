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