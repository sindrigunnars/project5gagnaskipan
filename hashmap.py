from bucket import *
class HashMap:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.map = [Bucket() for _ in range(self.capacity)]

    def __len__(self):
        return self.size

    def __setitem__(self, key, data):
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        if self.contains(key):
            return self.find(key)
        raise NotFoundException

    def _compress(self, key):
        return hash(key) % self.capacity

    def insert(self, key, data):
        self.rebuild()
        hash_val = self._compress(key)
        self.map[hash_val].insert(key, data)
        self.size += 1

    def update(self, key, data):
        hash_val = self._compress(key)
        self.map[hash_val].update(key, data)

    def find(self, key):
        hash_val = self._compress(key)
        return self.map[hash_val].find(key)

    def contains(self, key):
        hash_val = self._compress(key)
        return self.map[hash_val].contains(key)

    def remove(self, key):
        hash_val = self._compress(key)
        self.map[hash_val].remove(key)

    def rebuild(self):
        if self.size >= (self.capacity * 1.2):
            self.capacity *= 2
            temp = [Bucket() for _ in range(self.capacity)]
            for j in self.map:
                node = j.head
                while node != None:
                    hash_val = self._compress(node.key)
                    temp[hash_val].insert(node.key, node.data)
                    node = node.next
            self.map = temp

if __name__ == '__main__':
    m = HashMap()
    for i in range(10):
        m.insert(i * 5, f'{i}')
    m[10] = 'Hæ'
    for i in m.map:
        if i.head != None:
            print(i)