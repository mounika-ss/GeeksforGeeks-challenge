class Solution:
    def count(self, coins, Sum):
        # code here 
        # create a list of size Sum+1 and initialize all to 0
        dp = [0]*(Sum+1)
        
        # there is 1 way to make Sum = 0 (by taking no coins)
        dp[0] = 1
        
        # go through each coin
        for coin in coins:
            # update dp table from coin to target sum
            for amount in range(coin, Sum+1):
                dp[amount] += dp[amount-coin]
        # answer is number of ways to make sum = Sum target
        return dp[Sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        coins = list(map(int, input().strip().split()))
        sum = int(input())
        ob = Solution()
        print(ob.count(coins, sum))

        print("~")

# } Driver Code Ends
