#User function Template for python3
class Solution:
    
    def subarraySum(self, arr, target):
        n = len(arr)
        index = []
        start = end = 0
        
        current = 0
        for i in range(n):
            current = current + arr[i]
            if current >= target:
                end = i
                while current > target and start < end:
                    current -= arr[start]
                    start += 1
                if current == target:
                    index.append(start + 1)
                    index.append(end + 1)
                    return index
        return [-1]
            
#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends
