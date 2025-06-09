import heapq
from collections import defaultdict
class Solution:
    def findMinCycle(self, V, edges):
        mincycle = float('inf')
        for skip_u, skip_v, skip_w in edges:
            # rebuild graph without one edge
            graph = defaultdict(list)
            for u, v, w in edges:
                if (u == skip_u and v == skip_v and w == skip_w) or (u == skip_v and v == skip_u and w == skip_w):
                    continue
                graph[u].append((v, w))
                graph[v].append((u, w))
        
            # Dijikstra from skip_u to skip_v
            dist = [float('inf')] * V
            dist[skip_u] = 0
            pq = [(0, skip_u)]
            
            while pq:
                d, node = heapq.heappop(pq)
                if d>dist[node]:
                    continue
                for neighbor, weight in graph[node]:
                    if dist[neighbor] > dist[node] + weight:
                        dist[neighbor] = dist[node] + weight
                        heapq.heappush(pq, (dist[neighbor], neighbor))
            
            # if reachable, cycle found
            if dist[skip_v] != float('inf'):
                mincycle = min(mincycle, dist[skip_v] + skip_w)
        
        return mincycle if mincycle != float('inf') else -1
