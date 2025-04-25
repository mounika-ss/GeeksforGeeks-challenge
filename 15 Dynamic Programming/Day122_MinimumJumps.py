class Solution:
	def minJumps(self, arr):
        n = len(arr)
        
        # if array has one element or first element is 0
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        # maxreach is the farthest index reachable
        maxreach = arr[0]
        # steps we can still take before another jump
        step = arr[0]
        # number of jumps made
        jump = 1
        
        for i in range(1, n):
            # if we reach end of the array
            if i == n-1:
                return jump
            # update max reach 
            maxreach = max(maxreach, i+arr[i])
            # use step to move forward
            step = step - 1
            
            # if no more steps left
            if step == 0:
                jump = jump + 1 # we must jump now
                # if current index is beyond maxreach, return -1
                if i >= maxreach:
                    return -1
                # re-initialize steps
                step = maxreach - i
        return -1 # if we never reach end

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends
