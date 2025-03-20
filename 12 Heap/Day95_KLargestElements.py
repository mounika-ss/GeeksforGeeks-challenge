import heapq
class Solution:
	def kLargest(self, arr, k):
        minheap = []
        # build a min heap of size k
        for num in arr:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap) # remove the smallest element
        return sorted(minheap, reverse=True)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.kLargest(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends
