#User function Template for python3

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution():
    def cloneGraph(self, node):
        if not node:
            return None
        
        cloned = {}
        
        def dfs(curr):
            if curr in cloned:
                return cloned[curr]
            copy = Node(curr.val)
            cloned[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        return dfs(node)
