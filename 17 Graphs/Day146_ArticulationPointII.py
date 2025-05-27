from collections import defaultdict

class Solution:
    def articulationPoints(self, V, edges):
        # Articulation point
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # since its an undirected graph
        
        time = [0] # to maintain the discovery time
        disc = [-1] *V # discovery times
        low = [-1]*V # lowest discovery times reachable
        parent = [-1]*V
        ap = [False]*V # to mark articulation points
        
        def dfs(u):
            children = 0
            disc[u] = low[u] = time[0]
            time[0] += 1
            
            for v in adj[u]:
                # if v is not visited
                if disc[v] == -1:
                    parent[v] = u
                    children += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    
                    # u is root and has 2 or more children
                    if parent[u] == -1 and children>1:
                        ap[u] = True
                    # u is not root and low[v] >= disc[u]
                    if parent[u] != -1 and low[v]>=disc[u]:
                        ap[u] = True
                # update low[u] for back edge
                elif v != parent[u]:
                    low[u] = min(low[u], disc[v])
                    
        # run dfs for disconnected graph
        for i in range(V):
            if disc[i] == -1:
                dfs(i)
                
        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]
