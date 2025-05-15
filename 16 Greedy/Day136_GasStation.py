class Solution:
    def startStation(self, gas, cost):
        # Your code here
        totaltank = 0 # total fuel in the entire journey
        currtank = 0 # current fuel for the current segment
        startindex = 0 # starting station index
        
        for i in range(len(gas)):
            totaltank += gas[i] - cost[i]
            currtank += gas[i] - cost[i]
            
            # if current tank is negative, cant reach next station
            if currtank < 0:
                # try next station as the starting point
                startindex = i+1
                currtank = 0
            
        # if total tank is negative, journey is not possible
        return startindex if totaltank >= 0 else -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends
