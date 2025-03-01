#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends

#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # base case
        if e == 0:
            return 1.0
        if e<0:
            b = 1/b
            e = -e
        result = 1.0
        while e>0:
            if e%2 == 1:
                result *= b
            b *= b
            e //=2
        return result

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends
