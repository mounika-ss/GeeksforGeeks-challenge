# User function Template for Python3

class Solution:
    def search(self, arr, key):
        """
        Searches for a target key in a sorted and rotated array using binary search.
        Args:
        arr (list): A sorted and rotated array of distinct integers.
        key (int): The target value to find.

        Returns:
        int: The index of the target value if found; otherwise, -1.
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check if the mid element is the target
            if arr[mid] == key:
                return mid

            # Determine which half is sorted
            if arr[left] <= arr[mid]:
                # Left half is sorted
                if arr[left] <= key < arr[mid]:
                    right = mid - 1  # Key lies in the left half
                else:
                    left = mid + 1  # Key lies in the right half
            else:
                # Right half is sorted
                if arr[mid] < key <= arr[right]:
                    left = mid + 1  # Key lies in the right half
                else:
                    right = mid - 1  # Key lies in the left half

        # If the key is not found
        return -1

# Driver code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        A = list(map(int, input().strip().split()))  # Input array
        k = int(input())  # Key to search
        ob = Solution()
        print(ob.search(A, k))  # Print the index of the target key
        print("~")  # Separator for test case outputs
