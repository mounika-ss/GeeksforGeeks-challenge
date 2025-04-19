class Solution:
    def countWays(self, n):
        # code here
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        prev1 = 2 # ways to reach step 2
        prev2 = 1 # ways to reach step 1
        
        for i in range(3, n+1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        return prev1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends
