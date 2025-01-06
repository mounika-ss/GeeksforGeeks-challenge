class Solution:
    def mergeArrays(self, a, b):
        # Get the lengths of both arrays
        n, m = len(a), len(b)
        
        # Initial gap calculation
        gap = (n + m + 1) // 2

        # Keep reducing the gap until it is zero
        while gap > 0:
            i, j = 0, gap

            while j < (n + m):
                # If both pointers are in array 'a'
                if j < n and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

                # If pointers are across 'a' and 'b'
                elif i < n and j >= n and a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

                # If both pointers are in array 'b'
                elif i >= n and b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

                i += 1
                j += 1

            # Update the gap for the next iteration
            gap = (gap + 1) // 2 if gap > 1 else 0

        return a, b


# Driver Code (Unchanged)
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))

        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output the merged arrays
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))
        print("~")
