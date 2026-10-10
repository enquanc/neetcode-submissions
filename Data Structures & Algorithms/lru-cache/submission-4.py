class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}                  # key -> Node
        self.head = Node()               # dummy：最近用過的在它後面
        self.tail = Node()               # dummy：最久沒用的在它前面
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)               # 先拆下來
        self._add_to_front(node)         # 再放到最前面
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value             # 更新值
            self._remove(node)
            self._add_to_front(node)     # 視為剛用過
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)
            if len(self.cache) > self.capacity:
                lru = self.tail.prev     # 最久沒用的
                self._remove(lru)
                del self.cache[lru.key]  # dict 也要刪，所以 Node 要存 key