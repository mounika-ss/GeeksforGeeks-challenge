
class Solution:   
    def peakElement(self,arr):
        # Code here
        left, right = 0, len(arr)-1
        
        while left < right:
            mid = left + (right-left)//2
            
            # compare mid with its next element
            if arr[mid] < arr[mid+1]:
                # peak lies in the right half
                left = mid + 1
            else:
                # peak lies in the left half or is at mid
                right = mid
        
        # return the peak element's index
        return left
        
        
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
