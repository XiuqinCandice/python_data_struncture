class HashTable:
    # constructor
    def __init__(self):
        # size of the Hashable list
        self.slots = 10
        # current entries in the table
        # used while resizing the table when half of the table gets filled
        self.size = 0
        self.bucket = [None] * self.slots
    # Helper Functions

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.get_size() == 0

# Hash Function
def get_index(self, key):
    # hash is a built in function in Python
    hash_code = hash(key)
    index = hash_code % self.slots
    return index


ht = HashTable()
print(ht.is_empty())



a = 123

def reverse_digits(data):

    result = 0
    while data != 0:
        result = result *10 + data % 10
        data = data // 10
    
    return result
print(reverse_digits(a))
