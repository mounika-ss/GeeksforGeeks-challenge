# Python program to find majority elements in an array using Boyer-Moore Voting Algorithm.

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        # Using Boyer-Moore Voting Algorithm
        n = len(arr)
        ele1, ele2, c1, c2 = -1, -1, 0, 0  # Initialize two candidate elements and their counts
        
        # Identify potential candidates for majority elements
        for ele in arr:
            if ele1 == ele:
                c1 += 1
            elif ele2 == ele:
                c2 += 1
            elif c1 == 0:
                ele1, c1 = ele, 1
            elif c2 == 0:
                ele2, c2 = ele, 1
            else:
                c1 -= 1
                c2 -= 1

        # Verify the candidates by counting their actual occurrences
        result = []
        for ele in [ele1, ele2]:
            if arr.count(ele) > n // 3:
                result.append(ele)
        
        return sorted(result)
