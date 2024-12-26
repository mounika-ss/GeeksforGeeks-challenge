class Solution:
    def computeLPSArray(self, p):
        n = len(p)
        lps = [0] * n
        
        # lps[0] always 0
        length = 0
        
        i = 1
        while i < n:
            # if characters match, increment len and set lps[i]
            if p[i] == p[length]:
                length = length + 1
                lps[i] = length
                i = i + 1
            else:
                if length != 0:
                    # update length to the last known prefix length
                    length = lps[length - 1]
                # no prefix matches, set lps[i] to 0
                else:
                    lps[i] = 0
                    i = i + 1
        return lps
        
    def minChar(self, s):
        # we have to return an integer
        n = len(s)
        rev_s = s[::-1]
        
        # concatenation of string, special character and reverse string
        s = s + '$' + rev_s
        
        lps = self.computeLPSArray(s)
        
        return n - lps[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends
