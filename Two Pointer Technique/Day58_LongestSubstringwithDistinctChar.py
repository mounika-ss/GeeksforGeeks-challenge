#User function Template for python3
class Solution:
    MAX_CHAR = 26
    def longestUniqueSubstr(self, s):
        n = len(s)
        result = 0
        lastIndex = [-1]*self.MAX_CHAR
        start = 0
        
        for end in range(n):
            start = max(start, lastIndex[ord(s[end]) - ord('a')] + 1)
            result = max(result, end-start+1)
            lastIndex[ord(s[end]) - ord('a')] = end
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends
