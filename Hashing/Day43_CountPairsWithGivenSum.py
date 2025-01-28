class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Dictionary to store counts of elements
        counts = {}
        countpairs = 0
        
        # Iterate over each element in the array
        for ele in arr:
            complement = target - ele
            
            # Check if complement exists in the dictionary
            if complement in counts:
                countpairs += counts[complement]
            
            # Add the current element to the dictionary or update its count
            if ele in counts:
                counts[ele] += 1
            else:
                counts[ele] = 1
        
        return countpairs
