# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        prefixsum = 0
        prefixmap = {}
        maxlength = 0
        
        for i in range(len(arr)):
            prefixsum += arr[i]
            
            if prefixsum == k:
                maxlength = i+1
            if (prefixsum - k) in prefixmap:
                maxlength = max(maxlength, i-prefixmap[prefixsum - k])
            if prefixsum not in prefixmap:
                prefixmap[prefixsum] = i
        return maxlength
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends
