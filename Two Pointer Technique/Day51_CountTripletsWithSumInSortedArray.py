class Solution:
    def countTriplets(self, arr, target):
        # Using Two pointers technique
        n = len(arr)
        result = 0
        
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                summ = arr[i] + arr[left] + arr[right]
                if summ < target:
                    left += 1
                elif summ > target:
                    right -= 1
                else: 
                    e1 = arr[left]
                    e2 = arr[right]
                    count1 = 0
                    count2 = 0
                    while left <= right and arr[left] == e1:
                        left +=1
                        count1 += 1
                    while left <= right and arr[right] == e2:
                        right -= 1
                        count2 += 1
                    if e1 == e2:
                        result += (count1*(count1-1))//2
                    else:
                        result += (count1*count2)
        return result


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends
