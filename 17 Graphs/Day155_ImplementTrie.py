class TrieNode:
    def __init__(self):
        self.children = {}
        # True if this node marks the end of a word
        self.isEnd = False
      
#User function Template for python3
class Trie:
    def __init__(self):
        # implement Trie
        self.root = TrieNode()
        
    def insert(self, word: str):
        # insert word into Trie
        node = self.root
        for char in word:
            # if char not in children, add a new node
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True  # Mark end of the word
        

    def search(self, word: str) -> bool:
        # search word in the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                return False # character path not found
            node = node.children[char]
        return node.isEnd  # True only if exact word ends here

    def isPrefix(self, word: str) -> bool:
        # search prefix word in the Trie
        node = self.root
        for char in word:
            if char not in node.children:
                return False # prefix path not found
            node = node.children[char]
        return True # All prefix characters matched
