#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		n = len(mat) # length of matrix
		m = len(mat[0]) # length of row
		i = 0 # row
		j = m-1 # column
        
        while i < n and j >= 0:
            # if element > x then decrease column j
            if mat[i][j] > x:
                j = j - 1
            # if element < x then increase row i
            elif mat[i][j] < x:
                i = i + 1
            # if x present return true
            else: return True
        # if x not present then return false
        return False
        
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.matSearch(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends
