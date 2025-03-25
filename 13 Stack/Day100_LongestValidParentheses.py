
class Solution:
    def maxLength(self, s):
        # code here
        stack = [-1] # to handle edge cases
        maxlength = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # push index of '(' in s
                stack.append(i)
            else: # if char is ')'
                # pop the last '(' 
                stack.pop()
                if stack:
                    # update max length
                    maxlength = max(maxlength, i-stack[-1])
                else:
                    # push invalid ')' index
                    stack.append(i)
        return maxlength


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends
