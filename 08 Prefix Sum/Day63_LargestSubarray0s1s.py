class Solution:
    def maxLen(self, arr):
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                arr[i] = -1
        prefixsum = 0
        maxlength = 0
        sumIndexMap = {0:-1} #store prefix sum and its earliest index
        for i, num in enumerate(arr):
            prefixsum += num
            if prefixsum in sumIndexMap:
                maxlength = max(maxlength, i-sumIndexMap[prefixsum])
            else:
                sumIndexMap[prefixsum] = i
        return maxlength

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends
