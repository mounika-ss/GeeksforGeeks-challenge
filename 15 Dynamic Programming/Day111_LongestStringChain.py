#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # sort words based on their lengths
        words.sort(key=len)
        
        dp = {} # key: word, value: longest chain ending at this word
        maxlen = 1 # at least 1 word in a chain
        
        for word in words:
            dp[word] = 1 # minimum chain is the word itself
            for i in range(len(word)):
                prev = word[:i] + word[i+1:] # remove one letter
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev]+1)
            maxlen = max(maxlen, dp[word])
        return maxlen


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends
