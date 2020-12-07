'''
To implement a BST, the first thing you’d need is a node. 
A node should have a value, a left child, a right child, and a parent. 
This node can be implemented as a Python class and here is the code.

'''
class Node:
    def __init__(self, val):  # Constructor to initialize the value of the node
        self.val = val
        self.leftChild = None  # Sets the left and right children to `None`
        self.rightChild = None
    
    def insert(self, val):
        current = self
        parent = None
        while current:
            parent = current
            if val < current.val:
                current = current.leftChild
            else:
                current = current.rightChild

        if(val < parent.val):
            parent.leftChild = Node(val)
        else:
            parent.rightChild = Node(val)
    #iterative way
    def search(self, val):
        current = self
        while current:
            if val < current.val:
                current = current.leftChild
            elif val > current.val:
                current = current.rightChild
            else:
                return True
        return False
    #recursive way
    # def search(self, val):
    #     if val < self.val:
    #         if self.leftChild:
    #             return self.leftChild.search(val)
    #         else:
    #             return False
    #     elif val > self.val:
    #         if self.rightChild:
    #             return self.rightChild.search(val)
    #         else:
    #             return False
    #     else:
    #         return True
    #     return False #fully traversed, no self.val 

    def delete(self, val):
        if val < self.val:  # val is in the left subtree
            if(self.leftChild):
                self.leftChild = self.leftChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return None
        elif val > self.val:  # val is in the right subtree
            if(self.rightChild):
                self.rightChild = self.rightChild.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return None
        else:  # val was found
            #delete node with no children (leaf node)
            # delete leaf node by delete self and return None
            if self.leftChild is None and self.rightChild is None:
                self = None
                return None
            # delete node with right child only
            # delete node by delete self and return tmp (the right child node subsitutes its place)
            # replace its node with its right child by returning it
            elif self.leftChild is None:
                tmp = self.rightChild
                self = None
                return tmp
            # delete node with left child
            elif self.rightChild is None:
                tmp = self.leftChild
                self = None
                return tmp
            # delete a node with two children, find either the node with smallest value in the right sub-tree or the node with the largest value in the left sub-tree
            # use the way find the smallest value in the right sub-tree, do it by moving on to every node's left child until the last left child is reached
            # right sub-tree the very left is the closest to the node is going tot delete
            # same as the left-sub-tree, the very right is the closest to the node is going to be deleted

            else:
                current = self.rightChild
                # loop down to find the leftmost leaf
                while current.leftChild:
                    current = current.leftChild
                self.val = current.val
                self.rightChild = self.rightChild.delete(current.val)
        return self
