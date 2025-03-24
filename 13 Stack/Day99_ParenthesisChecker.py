class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        bracketmap = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            # if it is an opening bracket, push to stack
            if char in bracketmap.values(): 
                stack.append(char)
            # .if it is a closing bracket
            elif char in bracketmap.keys():
                # ṣtack empty or mismatch
                if not stack or stack[-1] != bracketmap[char]:
                    return False
                # remove matching open bracket
                stack.pop()
        # if stack is empty, brackets are balanced
        return not stack 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
