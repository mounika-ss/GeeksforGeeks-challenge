# User function Template for python3
class Solution:
    def check(self, stalls, k, dist):
        count = 1
        prev = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - prev >= dist:
                prev = stalls[i]
                count += 1
        return count >= k

    def aggressiveCows(self, stalls, k):
        # Using binary search
        stalls.sort()
        res = 0
        lo = 1
        hi = stalls[-1] - stalls[0]
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.check(stalls, k, mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
                
        return res


# { 
# Driver Code Starts
# Initial Template for Python 3
import bisect

# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends
