# User function Template for Python3

class Solution:
    def findMin(self, arr):
        # return min(arr) # for small arrays
        # if for large arrays use binary search
        left, right = 0, len(arr) - 1
        
        # if array is not rotated
        if arr[left] <= arr[right]:
            return arr[left]
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # check if the mid is the minimum
            if mid > 0 and arr[mid] < arr[mid - 1]:
                return arr[mid]
                
            # check if mid+1 is the minimum
            if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
                return arr[mid + 1]
                
            # if mid lies in the left sorted half
            if arr[mid] >= arr[left]:
                left = mid + 1
            else:
                right = mid - 1
                
        # return the left most element as fallback (this case should not occur for valid input)
        return arr[left]
                

# Driver Code
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")  # Output separator

if __name__ == "__main__":
    main()
