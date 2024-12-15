def getMinDiff(self, arr, k):
    n = len(arr)  # Number of towers
    # Step 1: Sort the array to make it easier to identify boundaries
    arr.sort()
    
    # Step 2: Initial difference between the tallest and shortest towers
    res = arr[n - 1] - arr[0]
    
    # Step 3: Traverse through the array, adjusting heights
    for i in range(1, len(arr)):
        # Skip towers where reducing height by k results in a negative value
        if arr[i] - k < 0:
            continue

        # Step 4: Calculate new minimum and maximum tower heights
        minH = min(arr[0] + k, arr[i] - k)
        maxH = max(arr[i - 1] + k, arr[n - 1] - k)

        # Step 5: Update the result with the smaller difference
        res = min(res, maxH - minH)
    
    return res  # Return the minimum possible difference
