class Solution:
    def maximumProfit(self, prices):
        result = 0
        min_val = prices[0]
        
        for i in range(1, len(prices)):
            # Calculate the profit if sold on day i
            profit = prices[i] - min_val
            
            # Update the result if the profit is greater
            if profit > result:
                result = profit
                
            # Update the min_val only if we find a new lower price
            if prices[i] < min_val:
                min_val = prices[i]

        return result
