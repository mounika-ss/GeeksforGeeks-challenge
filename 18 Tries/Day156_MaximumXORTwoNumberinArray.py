#User function Template for python3
class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def insert(self, num, root):
        node = root
        for i in range(31, -1, -1):
            # 32 bits for safety (since arr[i] <= 10^6)
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        
    def findMaxXOR(self, num, root):
        node = root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            opposite = 1-bit
            if opposite in node.children:
                max_xor |= (1 << i)
                node = node.children[opposite]
            else: node = node.children.get(bit, node)
        return max_xor
                
    def maxXor(self, arr):
        #code here
        root = TrieNode()
        max_result = 0
        # first insert all numbers into trie
        for num in arr:
            self.insert(num, root)
            
        # now find max XOR wwith eah number
        for num in arr:
            max_result = max(max_result, self.findMaxXOR(num, root))
            
        return max_result
