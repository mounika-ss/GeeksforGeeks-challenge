from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        maxvals = []
        n = len(arr)
        dq = deque()
        
        for i in range(n):
            # remove indices out of window
            while dq and dq[0] <= i-k:
                dq.popleft()
            # remove smaller values from back
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            # add current index
            dq.append(i)
            # add to result when window size reached
            if i >= k-1:
                maxvals.append(arr[dq[0]])
        return maxvals

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends
