#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        
        # initialize two variables to track min cost to reach current step
        first = cost[0]
        second = cost[1]
        
        for i in range(2, n):
            current = cost[i] + min(first, second)
            # move window forward
            first, second = second, current
        # minimum cost to reach top
        return min(first, second)

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends
