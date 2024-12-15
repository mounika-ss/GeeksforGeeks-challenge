# Python Code to left rotate an array using Reversal Algorithm

def rotateArr(arr, d):
    """
    Rotates an array to the left by d positions using the Reversal Algorithm.

    Parameters:
        arr (list): List of integers to be rotated
        d (int): Number of positions to rotate the array

    Returns:
        None: The array is rotated in place
    """
    n = len(arr)

    # Handle the case where d > size of the array
    d %= n

    # Reverse the first d elements
    reverse(arr, 0, d - 1)

    # Reverse the remaining n-d elements
    reverse(arr, d, n - 1)

    # Reverse the entire array
    reverse(arr, 0, n - 1)

def reverse(arr, start, end):
    """
    Helper function to reverse elements of the array in a given range.

    Parameters:
        arr (list): List of integers
        start (int): Starting index of the subarray
        end (int): Ending index of the subarray

    Returns:
        None: The subarray is reversed in place
    """
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    # Example input
    arr = [1, 2, 3, 4, 5, 6]
    d = 2
    
    # Call the rotateArr function
    rotateArr(arr, d)
  
    # Print the rotated array
    for i in range(len(arr)):
        print(arr[i], end=" ")

# Time Complexity: O(n), as we visit each element exactly twice.
# Auxiliary Space: O(1), since no additional space is used.
