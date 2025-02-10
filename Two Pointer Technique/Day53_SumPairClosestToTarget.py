#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        result = []
        left, right = 0, n-1
        mindif = float('inf')
        
        while left < right:
            summ = arr[left] + arr[right]
            if abs(target - summ) < mindif:
                mindif = abs(target - summ)
                result = [arr[left], arr[right]]
                
            if summ < target:    
                left = left + 1
            elif summ > target:
                right = right - 1
            else:
                return result
        
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends
