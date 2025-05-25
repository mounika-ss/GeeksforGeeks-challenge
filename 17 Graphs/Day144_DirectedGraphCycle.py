from collections import defaultdict
class Solution:
    def isCycle(self, V, edges):
        # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            
        # Create visited and recursion stack arrays
        visited = [False]*V
        rec_stack = [False]*V
        
        # Define DFS function to detect cycle
        def dfs(node):
            visited[node] = True
            rec_stack[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True # cycle found
                    
            rec_stack[node] = False
            return False
            
        # Check each component
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
