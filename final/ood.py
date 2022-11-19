import collections
from heapq import *
from datetime import datetime
import time


class LRUCache:
    def __init__(self, capacity: int):
        self.n = capacity
        self.d = {}
        self._data = []
        self.key = lambda x: x
        self.count = 0

    def put(self, key, val):
        if key in self.d.keys():
            keycount = self.d[key][1]+1
            self.d[key] = (val,keycount)
            self._keeptrack(key,keycount)
        else:
            if len(self.d) < self.n:
                self.d[key] = (val,1)
                self.count += 1
                self._keeptrack(key,1)
            else:
                del self.d[self._data.pop()[1]]
                self.count -= 1
                self.d[key] = (val,1)
                self.count += 1
                self._keeptrack(key,1)

    def get(self, key) -> int:
        if key in self.d.keys():
            keycount = self.d[key][1]+1
            self.d[key] = (self.d[key][0], keycount)
            self._keeptrack(key,keycount)
            return self.d[key][0]

        else:
            return -1

    def _keeptrack(self, key, accesscount=1) -> None:
        t = (self.key(-accesscount), key)
        if len(self._data) < self.n:
            heappush(self._data, t)
        else:
            # Equivalent to a push, then a pop, but faster
            heappushpop(self._data, t)

        print(self._data, self.d)


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)
cache.put(4, 4)  # evicts key 1
print(cache.get(1))  # returns -1 (not found)
print(cache.get(3))  # returns 3
print(cache.get(4))  # returns 4
