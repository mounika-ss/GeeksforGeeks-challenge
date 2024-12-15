# Python Program to move all zeros to the end using one traversal

def pushZerosToEnd(arr):
    """
    Function to move all zeroes in an array to the end
    while maintaining the order of non-zero elements.
    
    Parameters:
        arr (list): List of integers

    Returns:
        None: The function modifies the list in place
    """
    # Pointer to track the position for the next non-zero element
    count = 0
    
    # Traverse the array
    for i in range(len(arr)):
        # If the current element is non-zero
        if arr[i] != 0:
            # Swap the current element with the zero at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            # Move 'count' pointer to the next position
            count += 1

if __name__ == "__main__":
    # Example input
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    # Move zeroes to the end
    pushZerosToEnd(arr)
    # Print the modified array
    for num in arr:
        print(num, end=" ")  # Expected output: 1 2 4 3 5 0 0 0
