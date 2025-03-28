#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

class Solution:
    def calculateSpan(self, arr):
        #write code here
        n = len(arr)
        span = [0]*n
        stack = [] # stack to store indices
        for i in range(n):
            # pop elements from stack while stack is not empty
            # and the current price is greater than stack top
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # if stack is empty, all elements before arr[i] are smaller
            span[i] = i+1 if not stack else i-stack[-1]
            # push current index on to stack
            stack.append(i)
        return span
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends
