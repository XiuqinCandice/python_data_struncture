from Node import Node

class BinarySearchTree:
    def __init__(self, val):
        self.root = Node(val)

    def setRoot(self, val):
        self.root = Node(val)
    
    def getRoot(self):
        return self.root.get()
    
    def insert(self, val):
        if self.root:
            self.root.insert(val)
        else:
            self.root = Node(val)
            
    def search(self, val):
        if self.root:
            return self.root.search(val)
        else:
            return False
    def delete(self, val):
        if self.root:
            self.root = self.root.delete(val)
        else:
            return False
