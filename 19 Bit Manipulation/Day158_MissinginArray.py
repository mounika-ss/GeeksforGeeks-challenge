class Solution:
    def missingNum(self, arr):
        # code here
        # the actual size including missing number
        n = len(arr) + 1
        # sum of n natutal numbers
        total = n * (n + 1) // 2
        actual_sum = sum(arr)
        return total - actual_sum
