class Solution:
    def findUnique(self, arr):
        # code here 
        xor_sum = 0
        # xor all elements
        for num in arr:
            xor_sum ^= num
        return xor_sum
