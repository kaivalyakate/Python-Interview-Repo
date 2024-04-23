"""
LRU Cache - Heap Implementation
"""
from heapq import heappop, heappush
from collections import deque

class LRUCache:

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, val: int) -> None:
        pass


class LRUHeapCache(LRUCache):

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.map = {}
        self.q = deque()
        self.size = 0

    def get(self, key: int) -> int:
        val, use_count = self.map.get(key, (-1, -1))
        if val != -1:
            self.map[key] = (val, use_count + 1)
            self.q.append(key)
        return val
    
    def put(self, key: int, val: int) -> None:
        _, use_count = self.map.get(key, (-1, 0))
        if self.map.get(key, -1) == -1:
            self.size += 1
        self.map[key] = (val, use_count + 1)
        self.q.append(key)

        if self.size > self.capacity:
            self._evict_lru()
    
    def _evict_lru(self):
        while self.q:
            key = self.q.popleft()
            val, use_count = self.map.get(key)
            self.map[key] = (val, use_count - 1)

            if use_count - 1 == 0:
                self.map.pop(key)
                break


if __name__ == "__main__":
    cache: LRUCache = LRUHeapCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    print(cache.get(1))
    print(cache.get(2))
