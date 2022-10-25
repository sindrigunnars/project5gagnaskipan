class NotFoundException(Exception):
    pass

class ItemExistsException(Exception):
    pass

class Node:
    def __init__(self, key = None, data = None, next = None):
        self.data = data
        self.key = key
        self.next = next

class Bucket:
    def __init__(self, head = None):
        self.size = 0

    def __str__(self):
        ret_str = ''
        node = self.head
        while node != None:
            ret_str += f'{str(node.key)}: {str(node.data)}, '
            node = node.next
        return ret_str

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
    
    def insert(self, key, value):
        if not self.contains(key):
            node = Node(key, value, self.head)
            node.next = self.head
            self.head = node
            self.size += 1
            return
        raise ItemExistsException

    def update(self, key, data):
        temp = self.head
        while temp != None:
            if temp.key == key:
                temp.data = data
                return
            temp = temp.next
        raise NotFoundException
    
    def find(self, key):
        temp = self.head
        while temp != None:
            if temp.key == key:
                return temp.data
            temp = temp.next
        raise NotFoundException
    
    def contains(self, key):
        temp = self.head
        while temp != None:
            if temp.key == key:
                return True
            temp = temp.next
        return False

    def remove(self, key):
        if self.head == None or not self.contains(key):
            raise NotFoundException  

        if self.head.key == key:
            self.head = self.head.next
            return     

        temp = self.head
        while temp.next != None:
            if temp.next.key == key:
                temp.next = temp.next.next
                return
            temp = temp.next


if __name__ == '__main__':
    m = Bucket()
    m[1] = 1
    m[2] = 2
    m[5] = 5
    m[7] = 7
    m[3] = 3
    m[2] = 0
    print(m)
    m.remove(2)
    m.remove(1)
    m.remove(5)
    m.remove(7)