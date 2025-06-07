#User function template for Python

class Solution:
	def floydWarshall(self, dist):
        # number of nodes
        n = len(dist)
        # use the same as problem definition
        inf = 100000000
        
        # intermediate, source, destination nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != inf and dist[k][j] != inf:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
        return dist
