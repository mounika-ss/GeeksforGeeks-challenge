from collections import defaultdict
class Solution:
    def isBridge(self, V, edges, c, d):
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) # undirected
            
        def dfs(node, visited):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited)
        # Function to count connected components
        def count_components():
            visited = [False]*V
            count = 0
            for i in range(V):
                if not visited[i]:
                    dfs(i, visited)
                    count += 1
            return count
        
        # Count components before removing edge
        before = count_components()
        # Remove edge (c, d)
        graph[c].remove(d)
        graph[d].remove(c)
        # count components after removing edge
        after = count_components()
        # If number of components increases, its a bridge
        return after > before
