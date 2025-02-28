#User function Template for python3

# design the class in the most optimal way
from collections import deque
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()
        
    #Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        else:
            return -1
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            if len(self.cache) >= self.capacity:
                lru_key = self.order.pop()
                del self.cache[lru_key]
            self.cache[key] = value
            self.order.appendleft(key)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends
