class DoublyNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = {} # Ex: 1 : 'prev'.10.'next'
        # boundary declaration LRU, MRU 
        self.left = DoublyNode() # LRU
        self.right = DoublyNode() # MRU
        #connect these two boundaries together, empty cache
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        # Unlink the node from its current neighbors
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        ## Always insert the node right before the MRU
        prev_node = self.right.prev
        next_node = self.right
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1 
        node = self.cache_map[key]
        self.remove(node)
        self.insert(node) #now it's the most recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.remove(self.cache_map[key])
        node = DoublyNode(key, value)
        self.cache_map[key] = node
        self.insert(node)

        if len(self.cache_map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache_map[lru.key]
        
