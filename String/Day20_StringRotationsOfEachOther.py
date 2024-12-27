# User function Template for python3

class Solution:
    # Function to check if two strings are rotations of each other or not.
    def computeLPSArray(self, p):
        n = len(p)
        lps = [0] * n
        
        # length of the previous longest prefix suffix (lps)
        length = 0
        
        lps[0] = 0
        
        i = 1
        while i < n:
            # if characters match then increment length and extend the matching prefix
            if p[i] == p[length]:
                length = length + 1
                lps[i] = length
                i = i + 1
            # if there is no match
            else:
                if length != 0:
                    # update length to last known prefix length
                    length = lps[length - 1]
                # no prefix matches, set lps[i] = 0 and move to next char
                else:
                    lps[i] = 0
                    i = i + 1
        return lps

    def areRotations(self, s1, s2):
        # using KMP algorithm
        text = s1 + s1
        pat = s2
        
        n = len(text)
        m = len(pat)
        
        lps = self.computeLPSArray(pat)
        
        i = 0
        j = 0
        while i < n:
            if pat[j] == text[i]:
                j = j + 1
                i = i + 1
                
            if j == m:
                return True
                
            # mismatch after j matches
            elif i < n and pat[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i = i + 1
        return False


# { 
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = str(input())
        s2 = str(input())
        if (Solution().areRotations(s1, s2)):
            print("true")
        else:
            print("false")

# } Driver Code Ends
