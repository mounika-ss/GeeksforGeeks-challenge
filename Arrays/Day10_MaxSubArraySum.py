class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Using Kadane's Algorithm

        # Initialize the largest sum to the first element of the array
        lar_sum = arr[0]
        # Initialize the current sum to 0
        summ = 0

        # Iterate through each element in the array
        for i in range(len(arr)):
            # Add the current element to the running sum
            summ = summ + arr[i]
            # Update the largest sum if the running sum is greater
            if summ > lar_sum:
                lar_sum = summ
            # Reset the running sum to 0 if it becomes negative
            if summ < 0:
                summ = 0

        # Return the maximum subarray sum
        return lar_sum
