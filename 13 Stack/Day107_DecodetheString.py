class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop()+substr
                stack.pop()
                
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                stack.append(int(k)*substr)
        return ''.join(stack)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends
