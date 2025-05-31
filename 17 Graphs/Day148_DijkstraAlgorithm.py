import heapq
from collections import defaultdict

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Build adjacency list: u-> (v, weight)
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w)) # since the graph is undirected
            
        # initialize distance as infinity, except source
        dist = [float('inf')]*V
        dist[src] = 0
        # Minheap priority queue: (distance, node)
        pq = [(0, src)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            for v, weight in adj[u]:
                if dist[v] > current_dist + weight:
                    dist[v] = current_dist + weight
                    heapq.heappush(pq, (dist[v], v))
        return dist
