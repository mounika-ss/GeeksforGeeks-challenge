from collections import deque, defaultdict

class Solution:
	def isCycle(self, V, edges):
		# Code here
        # create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False]*V
        
        def bfs(start):
            queue = deque()
            queue.append((start, -1)) # (node, parent)
            visited[start] = True
            
            while queue:
                node, parent = queue.popleft()
                
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        # found a back edge, which means a cycle
                        return True
            return False
        
        # check for all components
        for i in range(v):
            if not visited[i]:
                if bfs(i):
                    return True
        return False
