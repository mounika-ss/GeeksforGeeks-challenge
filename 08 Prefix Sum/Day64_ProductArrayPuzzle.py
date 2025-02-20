#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n
        
        # calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
            
        # multiply with sufix products
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends
