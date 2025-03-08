#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
            
        # create a map to quickly find the index of any element in inorder
        inorder_index_map = {val:idx for idx, val in enumerate(inorder)}
        
        def build(preStart, preEnd, instart, inend):
            if preStart > preEnd or instart > inend:
                return None
            root_val = preorder[preStart]
            root = Node(root_val)
        
        
            # get index of root in inorder
            root_index = inorder_index_map[root_val]
            
            # number of elements in the left subtree
            left_size = root_index - instart
            
            # recursively construct the left and right subtrees
            root.left = build(preStart+1, preStart+left_size, instart, root_index-1)
            root.right = build(preStart+left_size+1, preEnd, root_index+1, inend)
            
            return root
        return build(0, len(preorder)-1, 0, len(inorder)-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends
