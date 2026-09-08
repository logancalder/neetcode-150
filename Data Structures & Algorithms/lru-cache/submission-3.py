class LRUCache:

    class Node:
        def __init__(self, value=-1, prev=None, nxt=None, key = -1):
            self.value = value
            self.prev = prev
            self.nxt = nxt
            self.key = key

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.cache: 
            dummy = self.cache[key]

            if dummy == self.tail:
                return dummy.value
            
            elif dummy == self.head:
                self.head = self.head.nxt
                self.head.prev = None
            
            else:
                dummy.prev.nxt = dummy.nxt
                dummy.nxt.prev = dummy.prev

            self.tail.nxt = dummy
            dummy.prev = self.tail
            dummy.nxt = None
            self.tail = dummy

            return dummy.value

        else: return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            
            if len(self.cache) >= self.capacity:
                lru = self.head
                del self.cache[lru.key]
                self.head = lru.nxt
                lru.prev = None

            dummy = self.Node(value, self.tail, None, key)

            if self.tail:
                self.tail.nxt = dummy
                self.tail = dummy
            else:
                self.head = dummy
                self.tail = dummy

            self.cache[key] = dummy

        else:
            self.cache[key].value = value
            self.get(key)
