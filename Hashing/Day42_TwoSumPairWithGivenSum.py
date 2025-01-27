#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# using hash set
		s = set()
		
		for ele in arr:
		    complement = target - ele
		    
		    if complement in s:
		        return True
            else:
                s.add(ele)
        # if no pair is found
        return False
		    
		    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
