#User function Template for python3

class Solution:
    def nQueen(self, n):
        def is_safe(board, row, col, n):
            for i in range(col):
                if board[i] == row or abs(board[i] - row) == abs(i-col):
                    return False
            return True
        def solve(col, board, solutions, n):
            if col == n:
                solutions.append(board[:])
                return
            for row in range(1, n+1):
                if is_safe(board, row, col, n):
                    board[col] = row
                    solve(col+1, board, solutions, n)
                    board[col] = 0
        solutions = []
        board = [0] * n
        solve(0, board, solutions, n)
        return solutions

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends
