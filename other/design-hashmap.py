class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sz = 1000
        self.t = [[] for _ in range(self.sz)]

    def find(self, key):
        h = self.hachage(key)
        for i, (k, v) in enumerate(self.t[h]):
            if k == key:
                return i, v
        return -1, -1

    def hachage(self, k: int):
        return k % self.sz

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i, _ = self.find(key)
        h = self.hachage(key)
        if i == -1:
            self.t[h].append((key, value))
        else:
            self.t[h][i] = (key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        _, v = self.find(key)
        return v

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i, _ = self.find(key)
        if i != -1:
            self.t[self.hachage(key)][i] = (key, -1)
