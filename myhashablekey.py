class MyHashableKey:
    def __init__(self, int_val, str_val):
        self.str_val = str_val
        self.int_val = int_val
    
    def __hash__(self):
        str_to_int = 0
        for i, j in enumerate(self.str_val):
            str_to_int += ((i+1) * ord(j))
        return int(str_to_int) + self.int_val

    def __eq__(self, other):
        return (other.str_val == self.str_val) and (other.int_val == self.int_val)
