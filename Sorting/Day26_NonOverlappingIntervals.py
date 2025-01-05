# { 
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        """
        Function to calculate the minimum number of intervals
        that need to be removed to make the remaining intervals
        non-overlapping.

        Parameters:
        intervals (list): List of intervals, where each interval
                          is represented as [start, end].

        Returns:
        int: Minimum number of intervals to be removed.
        """
        count = 0  # Initialize removal count
        intervals.sort()  # Sort intervals based on start times
        
        # Keep track of the end time of the last added interval
        end_val = intervals[0][1]
        
        # Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < end_val:
                # Current interval overlaps with the previous one
                count += 1  # Increment removal count
                # Update the end value to the minimum of current overlap
                end_val = min(intervals[i][1], end_val)
            else:
                # No overlap, update the end value
                end_val = intervals[i][1]
                
        return count  # Return the number of intervals removed
        

# { 
# Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        # Read number of intervals
        N = int(input())
        # Read the list of intervals
        intervals = [list(map(int, input().split())) for i in range(N)]
        # Create Solution object
        ob = Solution()
        # Get the result
        res = ob.minRemoval(intervals)
        # Print the result
        print(res)
        print("~")
# } Driver Code Ends
