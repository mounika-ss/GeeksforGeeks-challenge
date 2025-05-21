from collections import deque
class Solution:
	def orangesRotting(self, mat):
		#Code here
		n, m = len(mat), len(mat[0])
		queue = deque()
		fresh = 0
		
        # collect all initially rotten oranges and count fresh ones
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    queue.append((i, j, 0)) # (row, col, time)
                elif mat[i][j] == 1:
                    fresh += 1
        
        # BFS from all rotten oranges
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time_required = 0
        rotted = 0
        
        while queue:
            r, c, time = queue.popleft()
            time_required = max(time_required, time)
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<= nr<n and 0<=nc<m and mat[nr][nc] == 1:
                    mat[nr][nc] = 2
                    queue.append((nr, nc, time+1))
                    rotted += 1
        return time_required if rotted == fresh else -1

#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends
