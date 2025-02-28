#User function Template for python3

class Solution:
    def findPermutation(self, s):
        s = sorted(s)
        res = []
        self.backtrack(s, [], [False]*len(s), res)
        return res
    def backtrack(self, s, path, used, res):
        if len(path) == len(s):
            res.append(''.join(path))
            return
        for i in range(len(s)):
            # skip used characters or duplicates
            if used[i] or (i>0 and s[i] == s[i-1] and not used[i-1]):
                continue
            used[i] = True
            path.append(s[i])
            self.backtrack(s, path, used, res)
            path.pop()
            used[i] = False
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends
