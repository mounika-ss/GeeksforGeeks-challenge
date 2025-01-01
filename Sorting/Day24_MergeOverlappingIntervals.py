"""
Day 24: Merge Overlapping Intervals

Problem:
Given a list of intervals, merge all overlapping intervals and return the 
merged intervals in sorted order. This solution performs the merging in place, 
optimizing space usage.

Approach:
1. Sort the intervals based on their start times.
2. Traverse through the sorted intervals and merge overlapping ones by modifying 
   the original list in place.
3. Return the merged intervals.

Complexity:
- Time: O(n * log(n)) due to sorting.
- Space: O(1), as we perform the merging in place without additional storage.
"""

class Solution:
    def mergeOverlap(self, arr):
        # Step 1: Sort the array based on the start times
        arr.sort()

        # Step 2: Initialize the index for merged intervals
        resIdx = 0

        # Step 3: Traverse the intervals
        for i in range(1, len(arr)):
            # Check if the current interval overlaps with the last merged interval
            if arr[resIdx][1] >= arr[i][0]:
                # Merge the two intervals
                arr[resIdx][1] = max(arr[resIdx][1], arr[i][1])
            else:
                # No overlap, move resIdx to the next position and copy the current interval
                resIdx += 1
                arr[resIdx] = arr[i]

        # Return the merged intervals up to `resIdx + 1`
        return arr[:resIdx + 1]

if __name__ == '__main__':
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        n = int(input("Enter the number of intervals: "))
        arr = []
        for i in range(n):
            a = list(map(int, input().strip().split()))
            arr.append(a)
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        print("Merged Intervals:")
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()
