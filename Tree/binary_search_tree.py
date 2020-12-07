from Node import Node  # use `Node` class from Node.py


class BinarySearchTree:
    def __init__(self, val):  # Initializes a root node
        self.root = Node(val)

    def insert(self, val):
        if self.root:
            return self.root.insert(val)
        else:
            self.root = Node(val)
            return True
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
# BST = BinarySearchTree(6)  # Initializes a BST
# print(BST.root.val)  # print value of root node
