#User function Template for python3

# Node for linked list:

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Solution:
    def addTwoLists(self, num1, num2):
        def reverse(head):
            prev = None
            cur = head
            while cur:
                nextnode = cur.next
                cur.next = prev
                prev = cur
                cur = nextnode
            return prev
            
        # reverse both lists    
        num1 = reverse(num1)
        num2 = reverse(num2)
        carry = 0
        resulthead = None
        resulttail = None
        
        # add the numbers
        while num1 or num2 or carry:
            sumval = carry
            if num1:
                sumval += num1.data
                num1 = num1.next
            if num2:
                sumval += num2.data
                num2 = num2.next
                
            carry = sumval//10
            newnode = Node(sumval % 10)
            
            if resulthead is None:
                resulthead = newnode
                resulttail = newnode
            else:
                resulttail.next = newnode
                resulttail = newnode
        
        resulthead = reverse(resulthead)
        while resulthead and resulthead.data == 0 and resulthead.next:
            resulthead = resulthead.next
                
        return resulthead

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()


if __name__ == '__main__':
    for _ in range(int(input())):

        arr1 = (int(x) for x in input().split())
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)

        arr2 = (int(x) for x in input().split())
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)

        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
        print("~")

# } Driver Code Ends
