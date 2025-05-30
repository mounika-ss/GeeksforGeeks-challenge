import heapq
#User function Template for python3
class Solution:
    def minCost(self, houses):
        n = len(houses)
        # min heap to pick the minimum cost edge
        minheap = [(0, 0)] # (cost, house index)
        visited = [False]*n
        totalcost = 0
        edges_used = 0
        while edges_used <n:
            cost, u = heapq.heappop(minheap)
            if visited[u]:
                continue
            visited[u] = True
            totalcost += cost
            edges_used += 1
            
            # check all other houses not visited yet
            for v in range(n):
                if not visited[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    heapq.heappush(minheap, (dist, v))
        return totalcost
        
