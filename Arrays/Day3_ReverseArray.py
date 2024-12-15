# Python Program to reverse an array using Two Pointers

def reverseArray(arr):
    """
    Function to reverse an array in-place using the two-pointer approach.

    Parameters:
        arr (list): List of integers

    Returns:
        None: The array is reversed in place
    """
    # Initialize left to the beginning and right to the end
    left = 0
    right = len(arr) - 1

    # Iterate till left is less than right
    while left < right:
        # Swap the elements at left and right position
        arr[left], arr[right] = arr[right], arr[left]
        
        # Increment the left pointer
        left += 1

        # Decrement the right pointer
        right -= 1

if __name__ == "__main__":
    # Example input
    arr = [1, 4, 3, 2, 6, 5]
    
    # Call the reverseArray function
    reverseArray(arr)

    # Print the reversed array
    for i in range(len(arr)):
        print(arr[i], end=" ")

# Time Complexity: O(n), as we visit each element exactly once.
# Auxiliary Space: O(1), as no extra space is used.
