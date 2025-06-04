from collections import defaultdict, deque
class Solution:
    def findOrder(words):
        # buid the graph and collect all unique characters
        adj = defaultdict(set)
        indegree = {}
        
        # initialize indegree for all unique characters
        for word in words:
            for char in word:
                indegree[char] = 0
                
        # build adjacency list and update indegrees
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            minlen = min(len(word1), len(word2))
            for j in range(minlen):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
            else:
                if len(word1) > len(word2):
                    # invalid case like ["abc", "ab"]
                    return ""
                
        # topoogical Sort (kahns algorithm)
        q = deque([ch for ch in indegree if indegree[ch] == 0])
        result = []

        while q:
            ch = q.popleft()
            result.append(ch)
            for v in adj[ch]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    
        # if all letters are in result, return order; else invalid
        if len(result) == len(indegree):
            return ''.join(result)
        else:
            return ""
