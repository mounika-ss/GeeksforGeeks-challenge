#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        minheap = []
        
        # insert the first node of each linkedin list into the heap
        for head in arr:
            if head:
                heapq.heappush(minheap, head)
                
        dummy = Node(0) # dummy node to simplify list operations
        current = dummy # pointer to track the merged list
        
        # extract theminimum node and maintain the sorted order
        while minheap:
            smallest = heapq.heappop(minheap)
            current.next = smallest
            current = current.next
            
            # if there is a next node, push it into the heap
            if smallest.next:
                heapq.heappush(minheap, smallest.next)
                
        return dummy.next #return the merged linked list starting from the next node
        
#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
