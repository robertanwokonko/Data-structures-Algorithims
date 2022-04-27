from array import array


class hashTable:
    def __init__(self, size):
        self.data = [None]*size
        self.length = 0
        pass

    def get(self, key):
        return self.data[key]

    def set(self, key, value):

        self.address = hash(key)
        if self.address not in self.data:
            self.data[self.address] = 