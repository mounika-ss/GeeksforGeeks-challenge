# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        n = len(arr)
        result = [-1]*n
        stack = []
        
        for i in range(n-1, -1, -1): # traverse from right to left
            # remove smaller elements from stack
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            # if stack is not empty, top is the next greater element
            if stack:
                result[i] = stack[-1]
            # push current element on to the stack
            stack.append(arr[i])
        return result

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().nextLargerElement(arr)  # find the next greater elements

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print next greater elements
    else:
        print("[]")  # Print empty list if no next greater element is found
    print("~")
# } Driver Code Ends
