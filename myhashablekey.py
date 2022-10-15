class MyHashableKey:
    def __init__(self, int_val, str_val):
        self.int_val = int_val
        self.str_val = str_val
    
    def __hash__(self):
        str_to_int = 0
        for i in self.str_val:
            str_to_int += ord(i)
        # if self.int_val >= str_to_int:
        #     return self.int_val - str_to_int
        return str_to_int + self.int_val

    def __eq__(self, other):
        return (other.str_val == self.str_val) and (other.int_val == self.int_val)


m = MyHashableKey(104, 'h')
s = MyHashableKey(97, '1')
print(hash(m), hash(s))