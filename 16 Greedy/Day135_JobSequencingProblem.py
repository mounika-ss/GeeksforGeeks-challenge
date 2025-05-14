class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        
        # pair deadlines and profits
        jobs = list(zip(deadline, profit))
        
        # sort jobs by profit in descending order
        jobs.sort(key = lambda x: x[1], reverse = True)
        
        # find maximum deadline to create time slots
        max_deadline = max(deadline)
        parent = [i for i in range(max_deadline+1)] # disjoint set
        
        def find(slot):
            if parent[slot] == slot:
                return slot
            parent[slot] = find(parent[slot])
            return parent[slot]
            
        def union(u,v):
            parent[u] = v
            
        jobcount = 0
        totalprofit = 0
        
        # schedule each job
        for d, p in jobs:
            availableslot = find(d)
            if availableslot > 0:
                union(availableslot, availableslot-1)
                jobcount += 1
                totalprofit += p
                
        return [jobcount, totalprofit]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends
