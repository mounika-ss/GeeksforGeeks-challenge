class Solution:
    def isSubsetSum (self, arr, totalsum):
        # initialize a dp array with false values
        dp = [False] * (totalsum+1)
        # a sum of 0 is always possible
        dp[0] = True
        
        # loop through each element in arr
        for num in arr:
            # traverse backwards to avoid using the same number multiple times
            for j in range(totalsum, num-1, -1):
                if dp[j-num]:
                    dp[j] = True
        # return if sum is possible
        return dp[totalsum]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends
