#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
        xor_all = 0
        for num in arr:
            xor_all ^= num
            # xor of all elements, gives A^B (unique ones)
        
        # get rightmost set bit in xor_all (A^B)
        rightmost_set_bit = xor_all & -xor_all
        num1 = 0
        num2 = 0
        for num in arr:
            if num & rightmost_set_bit:
                num1 ^= num  # group 1
            else:
                num2 ^= num  # group 2
        
        return sorted([num1, num2])
