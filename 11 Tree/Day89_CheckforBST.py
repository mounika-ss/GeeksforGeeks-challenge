class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        # helper function to check the validity of BST with min and max constraints
        def check(node, minval, maxval):
            if not node:
            # or if node is None:
                return True
                
            # check if the current node's value is within the valid range
            # that is curr node violates the BST property
            if not (minval < node.data < maxval):
            # or if node.data <= minval or node.data >= maxval:
                return False
                
            # recursion for checking left and right subtrees
            # for left: valid range is [minval, node.data]
            # for right: valid range is [node.data, maxval]
            return check(node.left, minval, node.data) and check(node.right, node.data, maxval)
            # or return (check(node.left, minval, node.data) and check(node.right, node.data, maxval))
        
        # call function with full range of valid values
        return check(root, float('-inf'), float('inf'))


#{ 
 # Driver Code Starts
from collections import deque
import sys

sys.setrecursionlimit(10**8)


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    ip = list(map(str, s.split()))
    root = Node(int(ip[0]))
    q = deque()
    q.append(root)
    i = 1

    while i < len(ip):
        currNode = q.popleft()
        if ip[i] != "N":
            currNode.left = Node(int(ip[i]))
            q.append(currNode.left)
        i += 1
        if i < len(ip) and ip[i] != "N":
            currNode.right = Node(int(ip[i]))
            q.append(currNode.right)
        i += 1

    return root


# Main code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        if Solution().isBST(root):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends
