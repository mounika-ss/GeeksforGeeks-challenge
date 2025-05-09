#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        n = len(s)
        memo = {}
        
        def countwaysUtil(i, j, isTrue):
            if i>j:
                return 0
            if i == j:
                if isTrue:
                    return 1 if s[i] == 'T' else 0
                else: return 1 if s[i] == 'F' else 0
            key = (i, j, isTrue)
            if key in memo:
                return memo[key]
            
            ways = 0
            for k in range(i+1, j, 2):
                op = s[k]
                lt = countwaysUtil(i, k-1, True)
                lf = countwaysUtil(i, k-1, False)
                rt = countwaysUtil(k+1, j, True)
                rf = countwaysUtil(k+1, j, False)
                
                if op == '&':
                    if isTrue:
                        ways += lt*rt
                    else: ways += lt*rf + lf*rt + lf*rf
                elif op == '|':
                    if isTrue:
                        ways += lt*rt + lt*rf + lf*rt
                    else: ways += lf * rf
                elif op == '^':
                    if isTrue:
                        ways += lt*rf + lf*rt
                    else: ways += lt*rt + lf*rf
            memo[key] = ways
            return ways
        return countwaysUtil(0, n-1, True)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends
