
class Solution:
    def maxWater(self, arr):
        # using two pointers
        left = 1
        right = len(arr)-2
        lmax = arr[left-1]
        rmax = arr[right+1]
        
        result = 0
        while left <= right:
            if rmax <= lmax:
                result += max(0, rmax-arr[right])
                rmax = max(rmax, arr[right])
                
                right -= 1
            else:
                result += max(0, lmax-arr[left])
                lmax = max(lmax, arr[left])
                left += 1
        return result

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
