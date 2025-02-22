# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # edge case: empty list or k == 0
        if not head or k == 0:
            return head
            
        # find the length of the linked list
        temp = head
        length = 1
        while temp.next:
            temp = temp.next
            length += 1
            
        # adjust k if k>length
        k = k%length
        if k == 0:
            return head
            
        # find the new tail (length-k)th node
        temp = head
        for _ in range(k - 1):
            temp = temp.next
        
        # update head and break the link
        newhead = temp.next
        temp.next = None
        
        # connect the old tail to the old head
        temp = newhead
        while temp.next:
            temp = temp.next
        temp.next = head
        
        return newhead
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        k = int(data[idx + 1].strip())
        idx += 2
        head = Solution().rotate(head, k)
        printList(head)
        print("~")
        t -= 1

# } Driver Code Ends
