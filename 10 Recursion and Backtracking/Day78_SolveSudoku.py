#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        def is_valid(mat, row, col, num):
            for i in range(9):
                if mat[row][i] == num or mat[i][col] == num:
                    return False
                if mat[3*(row//3)+i//3][3*(col//3)+i%3]==num:
                    return False
            return True
        def solve():
            for row in range(9):
                for col in range(9):
                    if mat[row][col] == 0:
                        for num in range(1, 10):
                            if is_valid(mat, row, col, num):
                                mat[row][col] = num
                                if solve():
                                    return True
                                mat[row][col] = 0
                        return False
            return True
        solve()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends
