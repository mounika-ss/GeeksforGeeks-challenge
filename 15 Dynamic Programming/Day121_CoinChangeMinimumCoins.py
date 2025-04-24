class Solution:
	def minCoins(self, coins, sum):
		# initialize DP array with a large value
		dp = [float('inf')]*(sum+1)
        # 0 coins for sum 0
		dp[0] = 0
		
        # build up the dp array
        for coin in coins:
            for i in range(coin, sum+1):
                if dp[i-coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i-coin]+1)
        # if not possible to make the sum
        return -1 if dp[sum] == float('inf') else dp[sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends
