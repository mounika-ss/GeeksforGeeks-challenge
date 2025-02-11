#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        n = len(arr)
        left = 0
        right = n-1
        count = 0
        
        while left < right:
            if arr[left] + arr[right] < target:
                left = left + 1
            elif arr[left] + arr[right] > target:
                right = right - 1
            else:
                c1 = 0
                c2 = 0
                ele1 = arr[left]
                ele2 = arr[right]
                
                while left <= right and arr[left] == ele1:
                    left += 1
                    c1 += 1
                
                while left <= right and arr[right] == ele2:
                    right -= 1
                    c2 += 1
                    
                if ele1 == ele2:
                    count += (c1*(c1-1))//2
                else:
                    count += (c1*c2)
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
