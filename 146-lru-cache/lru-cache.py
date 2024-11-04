class Node:
    def __init__(self, key: int, value: int):
        self.key = key           
        self.value = value       
        self.prev = None         
        self.next = None         

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity                  
        self.cache = {}                           
        self.head, self.tail = Node(0, 0), Node(0, 0) 
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev      

    def _add(self, node: Node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]                
            self._remove(node)                    
            self._add(node)                       
            return node.value                     
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])         
        node = Node(key, value)                   
        self.cache[key] = node                    
        self._add(node)                           

        if len(self.cache) > self.capacity:
            lru = self.head.next                  
            self._remove(lru)                     
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)