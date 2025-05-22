#User function Template for python3
from collections import deque
class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0
            
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        # All 8 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
        (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited[row][col] = True
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (0<=nr<n and 0<=nc<m and not visited[nr][nc] and grid[nr][nc]=='L'):
                        visited[nr][nc] = True
                        queue.append((nr, nc))
        
        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    bfs(i, j)
                    island_count += 1
        return island_count
