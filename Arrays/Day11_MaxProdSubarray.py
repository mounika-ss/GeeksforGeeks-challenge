class Solution:
    # Function to find the maximum product subarray
    def maxProduct(self, arr):
        # Initialize variables
        lr, rl, maxi = 1, 1, float('-inf')  # Left-to-right, right-to-left products, and max product
        n = len(arr)

        for i in range(n):
            # Reset products to 1 if they encounter 0
            if lr == 0:
                lr = 1
            if rl == 0:
                rl = 1

            # Calculate products from both ends
            lr *= arr[i]
            rl *= arr[n - 1 - i]

            # Update the maximum product encountered
            maxi = max(maxi, lr, rl)

        return maxi
