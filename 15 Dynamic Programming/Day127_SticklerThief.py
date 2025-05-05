class Solution:  
    def findMaxSum(self,arr):
        # code here
        if not arr:
            return 0
        incl = arr[0]
        excl = 0
        
        for i in range(1, len(arr)):
            newincl = excl + arr[i]
            newexcl = max(incl, excl)
            
            incl = newincl
            excl = newexcl
        return max(incl, excl)


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends
