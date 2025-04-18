class Solution:
	def editDistance(self, s1, s2):
		# Code here
		n, m = len(s1), len(s2)
		# create a (n+1) x (m+1) DP table
		dp = [[0]*(m+1) for _ in range(n+1)]
		
		# if string is empty, we need to insert all characters of other
		# or delete all characters
		for i in range(n+1):
		    dp[i][0] = i # need i deletions
		for j in range(m+1):
		    dp[0][j] = j # need j insertions
            
        # fill the table 
        for i in range(1, n+1):
            for j in range(1, m+1):
                # if characters match, no operation needed
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1] + 1
                    delete = dp[i-1][j]+1
                    replace = dp[i-1][j-1]+1
                    dp[i][j] = min(insert, delete, replace)
        return dp[n][m]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends
