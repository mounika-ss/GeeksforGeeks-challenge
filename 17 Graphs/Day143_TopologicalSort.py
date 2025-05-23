from collections import deque, defaultdict
class Solution:
    def topoSort(self, V, edges):
        # create adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            
        # calculate indegree for each node
        indegree = [0]*V
        for u in adj:
            for v in adj[u]:
                indegree[v] += 1
                
        # add all nodes with 0 indegree to queue
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        # process nodes from queue
        topoOrder = []
        while queue:
            node = queue.popleft()
            topoOrder.append(node)
            
            # reduce indegree of adjacent nodes
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # if we could sort all nodes, return the result
        if len(topoOrder) == V:
            return topoOrder
        else:
            return [] # if not all nodes processed, there was a cycle
