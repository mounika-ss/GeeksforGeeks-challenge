class Solution:
    def wordBreak(self, s, dictionary):
        n = len(s)
        maxlen = max(map(len, dictionary)) 
        wordset = set(dictionary)
        dp =  [False]*(n+1)
        dp[0] = True # empty string always "breakable"
        
        for i in range(1, n+1):
            for j in range(max(0, i-maxlen), i): # only check within the word
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        s = input().strip()
        dictionary = input().strip().split()
        ob = Solution()
        res = ob.wordBreak(s, dictionary)
        if res:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends
