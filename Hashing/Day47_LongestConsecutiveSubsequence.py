# User function Template for Python3

class Solution:
    
    # Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self, arr):
        set_ = set()
        ans = 0
        
        # Copying elements into the set
        for i in arr:
            set_.add(i)
            
        for i in range(len(arr)):
            # Checking if it's the starting element of a sequence
            if (arr[i] - 1) not in set_:
                j = arr[i]
                
                # Counting the length of the sequence
                while j in set_:
                    j += 1
                    
                ans = max(ans, j - arr[i])
                
        return ans


# Driver Code
import sys
import io
import atexit

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
