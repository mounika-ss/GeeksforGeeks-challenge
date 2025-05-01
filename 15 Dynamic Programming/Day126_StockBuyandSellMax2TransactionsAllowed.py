class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        
        # create two lists to store max profit from left and right
        left = [0]*n
        right = [0]*n
        
        # left pass: max profit if sold up to day i (1st transaction)
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            left[i] = max(left[i-1], prices[i]-minprice)
            
        # right pass: max profit if bought from day i (2 transaction)
        maxprice = prices[n-1]
        for i in range(n-2, -1, -1):
            maxprice = max(maxprice, prices[i])
            right[i] = max(right[i+1], maxprice-prices[i])
            
        # combine both for max total profit
        maxprofit = 0
        for i in range(n):
            maxprofit = max(maxprofit, left[i]+right[i])
        return maxprofit
#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
