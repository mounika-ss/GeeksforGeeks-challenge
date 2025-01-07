"""
Problem: Count the occurrences of a target in a sorted array.

Input:
- A sorted array (arr).
- A target integer.

Output:
- The count of occurrences of the target.

Approach:
1. Use binary search to find the first occurrence of the target.
2. Use binary search to find the last occurrence of the target.
3. Calculate the count as (last_occurrence - first_occurrence + 1).
"""
class Solution:
    def countFreq(self, arr, target):
        def first_occurrence(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def last_occurrence(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_index = first_occurrence(arr, target)
        right_index = last_occurrence(arr, target)

        if left_index <= right_index and right_index < len(arr) and arr[left_index] == target:
            return right_index - left_index + 1
        return 0

# Driver Code
if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        print(ob.countFreq(arr, target))
