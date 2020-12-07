from Node import Node
from binary_search_tree import BinarySearchTree


def findKNodes(root, k):
    res = []
    find_nodes(root,k,res)
    return res

def find_nodes(root,k,res):
    if root is None:
        return 
    if k ==0:
        res.append(root.val)

    else:
        find_nodes(root.leftChild,k-1,res)
        find_nodes(root.rightChild,k-1,res)

BST = BinarySearchTree(6)
BST.insert(4)
BST.insert(9)
BST.insert(5)
BST.insert(2)
BST.insert(8)
BST.insert(12)
print(findKNodes(BST.root, 2))