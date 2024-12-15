# Day 5: Next Permutation Algorithm

# Observations:
# 1. To get the next permutation, we change the rightmost number that's smaller than its next.
# 2. If no such element exists, reverse the array to get the smallest permutation.
# 3. Otherwise, find the rightmost greater element, swap, and reverse the suffix.

def next_permutation(arr):
    n = len(arr)

    # Find pivot
    pivot = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            pivot = i
            break

    # Reverse if pivot does not exist
    if pivot == -1:
        arr.reverse()
        return

    # Find the element to swap with pivot
    for i in range(n - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    # Reverse the suffix part
    left, right = pivot + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [2, 4, 1, 7, 5, 0]
next_permutation(arr)
print(" ".join(map(str, arr)))

# Time Complexity:
# O(n) where n is the size of the array.

# Space Complexity:
# O(1) as the algorithm operates in-place (does not use additional space).
