#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        # Initialize distances
        dist = [float('inf')]*V
        dist[src] = 0
        
        # relax all edges V-1 times
        for _ in range(V-1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w<dist[v]:
                    dist[v] = dist[u] + w
        # check for negative weight cycle
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w<dist[v]:
                return [-1] # negative cycle found
        
        # replace unreachable nodes with 1e8
        return [d if d!=float('inf') else int(1e8) for d in dist]
