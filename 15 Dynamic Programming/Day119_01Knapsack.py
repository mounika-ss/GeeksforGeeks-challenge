class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n = len(val)
        
        # create a 2D dp table of size (n+1) X (W+1)
        dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
        
        # build the table in bottom-up manner
        # loop througheach item
        for i in range(1, n+1):
            # loop through each capacity from 0 to W
            for w in range(W+1):
                if wt[i-1] <= w:
                    # option to include or exclude the item
                    dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
                else:
                    # can't include the item
                    dp[i][w] = dp[i-1][w]
        
        # final answer is at the bottom-right corner
        return dp[n][W]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        capacity = int(input())
        values = list(map(int, input().strip().split()))
        weights = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapsack(capacity, values, weights))
        print("~")
# } Driver Code Ends
