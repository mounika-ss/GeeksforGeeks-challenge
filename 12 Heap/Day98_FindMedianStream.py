import heapq

class Solution:
    def getMedian(self, arr):
        rightminheap = [] # stores the larger half (right side)
        leftmaxheap = [] # stores the smaller half (left side)
        medians = []
        
        for num in arr:
            # insert into appropriate heap
            if not leftmaxheap or num <= -leftmaxheap[0]: # insert into maxheap
                heapq.heappush(leftmaxheap, -num)
            else: # insert into minheap
                heapq.heappush(rightminheap, num)
            
            # .balance heaps if necessary
            if len(leftmaxheap) > len(rightminheap) + 1:
                heapq.heappush(rightminheap, -heapq.heappop(leftmaxheap))
            elif len(rightminheap) > len(leftmaxheap):
                heapq.heappush(leftmaxheap, -heapq.heappop(rightminheap))
            
            # find median
            if len(leftmaxheap) > len(rightminheap):
                medians.append(float(-leftmaxheap[0]))
            else:
                medians.append((float(-leftmaxheap[0]) + float(rightminheap[0])) / 2.0)
        return medians

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends
