from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        #code here 
        maxDeque = deque()
        minDeque = deque()
        left = 0
        start = 0
        maxlen = 0
        
        for right in range(len(arr)):
            # maintain decreasing deque for max
            while maxDeque and arr[right] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(arr[right])
            
            # maintain increasing deque for min
            while minDeque and arr[right] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(arr[right])
            
            # shrink window if condition breaks
            while maxDeque[0] - minDeque[0] >x:
                if maxDeque[0] == arr[left]:
                    maxDeque.popleft()
                if minDeque[0] == arr[left]:
                    minDeque.popleft()
                left += 1
            # update longest subarray
            if right-left+1 > maxlen:
                maxlen = right-left+1
                start = left
        return arr[start:start+maxlen]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
