# User function template for Python3
class Solution:
    def kthMissing(self, arr, k):
        """
        Finds the kth missing positive integer in a sorted array.

        :param arr: List[int] - A sorted array of distinct positive integers.
        :param k: int - The position (kth) of the missing number to find.
        :return: int - The kth missing positive integer.
        """

        # Initialize the binary search bounds
        low = 0
        high = len(arr) - 1
        # Initialize the result to the position assuming all elements are missing
        result = len(arr) + k

        # Perform binary search
        while low <= high:
            mid = (low + high) // 2  # Find the middle index

            # Check if the number of missing elements before arr[mid] >= k
            if arr[mid] > mid + k:
                # Update the result to the potential kth missing number
                result = mid + k
                # Search the left side
                high = mid - 1
            else:
                # Search the right side
                low = mid + 1

        return result


# Driver code
if __name__ == '__main__':
    # Number of test cases
    t = int(input("Enter number of test cases: "))
    while t:
        t -= 1
        # Read the sorted array of integers
        A = [int(x) for x in input("Enter the array: ").strip().split()]
        # Read the value of k
        nd = [int(x) for x in input("Enter the value of k: ").strip().split()]
        D = nd[0]
        
        # Create an instance of the Solution class
        ob = Solution()
        # Call the method to find the kth missing number
        ans = ob.kthMissing(A, D)
        # Print the result
        print(f"The {D}th missing positive number is: {ans}")
        print("~")
