class Solution:
    def equalPartition(self, arr):
        n = len(arr)
        arrsum = sum(arr)
        # if sum of all elements in the array is odd then there will be chance to not be the equal parts
        if arrsum%2 != 0:
            return False
        
        target = arrsum//2
        
        # dp array to store if a sum is possible 
        dp = [False] * (target+1)
        dp[0] = True # zero sum is always possible
        
        for num in arr:
            for j in range(target, num-1, -1):
                if dp[j-num]:
                    dp[j] = True
        return dp[target]


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
