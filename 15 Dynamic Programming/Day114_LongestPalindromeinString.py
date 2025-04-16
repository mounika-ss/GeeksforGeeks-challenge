class Solution:
    def longestPalindrome(self, s):
        # code here
        n = len(s)
        if n == 0:
            return ''
        
        # initialize a table to store palindrome truth values
        dp = [[False]*n for _ in range(n)]
        # to store the starting index of the longest palindrome
        start = 0
        # length of the longest palindrome
        maxlen = 1
        
        # all substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            
        # check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                maxlen = 2
        # check for substrings longer than 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > maxlen:
                        start = i
                        maxlen = length
                        
        return s[start:start+maxlen]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends
