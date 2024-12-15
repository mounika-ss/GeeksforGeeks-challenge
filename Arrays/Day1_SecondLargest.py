"""
Day 1: Find the Second Largest Element
GeeksforGeeks Challenge
"""

# Problem Description:
# Given an array, find the second largest element.
# If there is no second largest, return -1.

def findSecondLargest(arr):
    """
    Function to find the second largest element in an array.
    
    Parameters:
    arr (list): List of integers
    
    Returns:
    int: The second largest element or -1 if not applicable.
    """
    if len(arr) < 2:
        return -1

    first, second = float('-inf'), float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else -1

# Driver Code
if __name__ == "__main__":
    # Test Case
    arr = [1, 2, 4, 3]
    print(f"The second largest element is: {findSecondLargest(arr)}")
