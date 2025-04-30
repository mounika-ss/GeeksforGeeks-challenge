class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n == 0 or k == 0:
            return 0
        
        # if k is large enough, it becomes an unlimited transaction problem
        if k >= n//2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit = profit + (prices[i] - prices[i-1])
            return profit
        # DP table: dp[transaction][day]
        dp = [[0]* n for _ in range(k+1)]
        
        for t in range(1, k+1):
            maxdiff = -prices[0]
            for d in range(1, n):
                dp[t][d] = max(dp[t][d-1], prices[d] + maxdiff)
                maxdiff = max(maxdiff, dp[t-1][d] - prices[d])
        return dp[k][n-1]

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends
