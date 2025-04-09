from bisect import bisect_left

class Solution:
    def lis(self, arr):
        tail = []
        
        for num in arr:
            index = bisect_left(tail, num) # find where this number fits in the list
            
            if index == len(tail):
                # if num is greater than all elements in the tail, add it at end
                tail.append(num)
            else:
                # otherwise, replace the first element in tail which is >=num
                tail[index] = num
        return len(tail)
        
#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends
