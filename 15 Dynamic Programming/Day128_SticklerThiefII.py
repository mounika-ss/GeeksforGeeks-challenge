class Solution:
    def maxloot(self, nums):
        # code here
        prev1 = 0 # loot till i-1
        prev2 = 0 # loot till i-2
        for num in nums:
            temp = max(prev1, prev2+num)
            prev2 = prev1
            prev1 = temp
        return prev1
    
    def maxValue(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        
        # option 1: exclude last house
        loot1 = self.maxloot(arr[:-1])
        # option 2: exclude first house
        loot2 = self.maxloot(arr[1:])
        
        return max(loot1, loot2)
        
#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends
