class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # dp[i][j] = minimum cost to multiply matrices from i to j
        for length in range(2, n): #chain length
            for i in range(1, n-length+1):
                j = i+length-1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                    dp[i][j] = min(dp[i][j], cost)
        return dp[1][n-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends
