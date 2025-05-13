class Solution:
    def activitySelection(self, start, finish):
        # pair up start and finish times
        activities = list(zip(start, finish))
        
        # sort activities by their finish times
        activities.sort(key = lambda x: x[1])
        count = 0
        last_end = 0
        for s, f in activities:
            if s > last_end:
                count += 1
                last_end = f
        return count

#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
