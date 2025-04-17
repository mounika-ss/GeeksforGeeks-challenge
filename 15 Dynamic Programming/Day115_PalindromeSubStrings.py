#User function Template for python3

class Solution:

    def countPS(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0
        # every single character is palindrome
        for i in range(n):
            dp[i][i] = True
        
        # check for substrings of length >=2
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1 # endpoint of the substring
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                    
                    if dp[i][j]:
                        count += 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.countPS(s))

        print("~")
# } Driver Code Ends
