class Solution:
    
    # Function to find minimum number of pages.
    def check(self, arr, k, pageLimit):
        count = 1
        pageSum = 0
        for pages in arr:
            if pageSum + pages > pageLimit:
                count += 1
                pageSum = pages
            else:
                pageSum += pages
        return count <= k
    
    def findPages(self, arr, k):
        # Using binary search
        if k > len(arr):
            return -1
            
        maxx = max(arr)
        summ = sum(arr)
        res = -1
        
        while maxx <= summ:
            mid = maxx + (summ - maxx) // 2
            
            if self.check(arr, k, mid):
                res = mid
                summ = mid - 1
            else:
                maxx = mid + 1
                
        return res



#{ 
 # Driver Code Starts
# Initial Template for Python 3
import bisect
# Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends
