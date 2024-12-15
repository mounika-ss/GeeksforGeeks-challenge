# Python program to calculate maximum profit from stock prices.

class Solution:
    def maximumProfit(self, prices) -> int:
        profit = 0
        
        # Traverse through the prices list and add profits if possible
        for i in range(len(prices)-1):
            # Check if profit can be made (price goes up)
            if prices[i+1] > prices[i]:
                # Add the profit (price difference)
                profit = profit + (prices[i+1] - prices[i])
        
        return profit
