class Solution:
    def intersectionWithDuplicates(self, a, b):
        # Convert array b into a set for O(1) lookups
        set_b = set(b)
        result = set()

        # Iterate through a and check if element exists in set_b
        for i in a:
            if i in set_b:
                result.add(i)

        return list(result)
