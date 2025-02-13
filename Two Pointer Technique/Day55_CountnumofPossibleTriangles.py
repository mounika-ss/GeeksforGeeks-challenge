#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        result = 0
        arr.sort()
        
        for i in range(2, len(arr)):
            left, right = 0, i-1
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends
