#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        # repetitive element
        n = len(arr)
        xor_all = 0
        
        # xor all elements from 1 to n-1
        for i in range(1, n):
            xor_all ^= i
        
        # xor with all elements in array
        for num in arr:
            xor_all ^= num
            
        return xor_all
