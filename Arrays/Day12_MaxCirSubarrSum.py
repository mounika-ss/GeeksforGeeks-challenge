class Solution:
    def maxSubarraySumCircular(self, arr):
        # Function to calculate max subarray sum using Kadane's Algorithm
        def kadane(nums):
            max_sum = cur_sum = nums[0]
            for num in nums[1:]:
                cur_sum = max(num, cur_sum + num)  # Compare current number with cumulative sum
                max_sum = max(max_sum, cur_sum)   # Update max sum so far
            return max_sum

        total_sum = sum(arr)  # Sum of all elements in the array
        max_kadane = kadane(arr)  # Standard max subarray sum using Kadane's algorithm
        
        # Invert the array to calculate the minimum subarray sum
        arr_inverted = [-num for num in arr]  # Change signs of all elements
        min_subarray_sum = kadane(arr_inverted)  # Find min subarray sum using Kadane
        max_circular = total_sum + min_subarray_sum  # Adjusted for circular subarray

        # Edge case: Handle case where all elements are negative
        if max_circular == 0:
            return max_kadane

        # Return the larger of two: non-circular max sum or circular max sum
        return max(max_kadane, max_circular)

# Example usage
sol = Solution()
arr = [8, -8, 9, -9, 10, -11, 12]
print(sol.maxSubarraySumCircular(arr))  # Output: 22
