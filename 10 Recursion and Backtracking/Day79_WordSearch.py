class Solution:
	def isWordExist(self, mat, word):
	    rows, cols = len(mat), len(mat[0])
	    def dfs(r, c, index):
	        if index == len(word):
	            return True
            if r<0 or r>= rows or c<0 or c>= cols or mat[r][c] != word[index]:
                return False
            temp = mat[r][c]
            mat[r][c] = '#'
            
            # explore in all 4 directions
            found = (dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1))
            # restore the cell
            mat[r][c] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
