#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

class Solution:
    def evaluate(self, arr):
        # stack to store numbers
        stack = []
        
        # iterate through each element
        for ele in arr:
            if ele in "+-*/":
                b = stack.pop()
                a = stack.pop()
                
                if ele == '+':
                    stack.append(a+b)
                elif ele == '-':
                    stack.append(a-b)
                elif ele == '*':
                    stack.append(a*b)
                elif ele == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(ele))
                
        # return first element as the answer
        return stack[0]
                

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends
