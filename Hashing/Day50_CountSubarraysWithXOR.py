class Solution:
    def subarrayXor(self, arr, k):
        result = 0
        mydict = {}
        prefixXOR = 0
        for i in arr:
            prefixXOR ^= i
            result += mydict.get(prefixXOR ^ k, 0)
            if prefixXOR == k:
                result += 1
            mydict[prefixXOR] = mydict.get(prefixXOR, 0)+1
        return result

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends
