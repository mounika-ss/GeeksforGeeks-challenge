class Solution:
    def maxPartitions(self , s):
        # record last index of each character
        lastindex = {char:idx for idx, char in enumerate(s)}
        
        partitions, end, start = 0, 0, 0
        
        # traverse string and decide partition points
        for i, char in enumerate(s):
            end = max(end, lastindex[char]) # expand the window
            
            # when current index matches partition end, we can split
            if i == end:
                partitions +=1
                start = i+1 # start of next partition
        return partitions

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends
