class Solution:
    def missingNumber(self, arr):
        # Get the length of the array
        n = len(arr)

        # Step 1: Place each number in its correct index position
        for i in range(n):
            # While the number is within the range [1, n] and not in its correct index
            while (1 <= arr[i] <= n) and (arr[arr[i] - 1] != arr[i]):
                # Swap the number to its correct index
                arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        
        # Step 2: After the swaps, find the first index where arr[i] != i + 1
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        # Step 3: If all elements from 1 to n are placed correctly, return n + 1
        return n + 1
