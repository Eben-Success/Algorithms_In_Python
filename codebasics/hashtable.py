class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [None for i in range(self.Max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
            return hash % self.Max

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


