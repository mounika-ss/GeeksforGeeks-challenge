#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self,arr):
        #code here
        stack = []
        maxarea = 0
        n = len(arr)
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                height = arr[stack.pop()]
                width = i if not stack else i-stack[-1] -1
                maxarea = max(maxarea, height*width)
            stack.append(i)
            
        while stack:
            height = arr[stack.pop()]
            width = n if not stack else n-stack[-1] - 1
            maxarea = max(maxarea, height*width)
        return maxarea


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends
