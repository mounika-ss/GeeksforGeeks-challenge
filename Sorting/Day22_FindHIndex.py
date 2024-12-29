# User function Template for Python3

class Solution:
    # Function to find H-Index
    def hIndex(self, citations):
        """
        This function calculates the H-Index for a researcher based on the given citations array.
        
        Parameters:
        citations (list): An array where each element represents the number of citations for a paper.

        Returns:
        int: The H-Index value, which is the largest value H such that the researcher has at least H 
             papers with at least H citations each.
        """
        n = len(citations)  # Number of papers
        freq = [0] * (n + 1)  # Array to store frequencies, size n+1 to account for citations > n

        # Populate the frequency array
        for i in citations:
            # If citations are greater than the number of papers, count it in the last bucket
            if i > n:
                freq[n] += 1
            else:
                # Count citations at the respective index
                freq[i] += 1

        # Traverse the frequency array from the end to the beginning
        index = n  # Start with the maximum possible H-Index
        count = freq[n]  # Initialize with the count from the last bucket
        while count < index:
            # Combine the counts of current and previous buckets
            index -= 1
            count += freq[index]

        # Return the H-Index
        return index


# Driver Code Starts
if __name__ == '__main__':
    """
    Main execution starts here. It takes the input for test cases and citations for each researcher.
    """
    t = int(input())  # Number of test cases
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]  # Input array of citations

        ob = Solution()  # Create an instance of the Solution class
        result = ob.hIndex(arr)  # Calculate H-Index

        print(result)  # Output the H-Index for the current test case
        print("~")
