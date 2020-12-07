from Node import Node
from binary_search_tree import BinarySearchTree
import random


def display(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.rightChild is None and node.leftChild is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.rightChild is None:
        lines, n, p, x = _display_aux(node.leftChild)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.leftChild is None:
        lines, n, p, x = _display_aux(node.rightChild)
        s = str(node.val)
        u = len(s)
#        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.leftChild)
    right, m, q, y = _display_aux(node.rightChild)
    s = '%s' % node.val
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * \
        '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + \
        (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + \
        [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


# BST = BinarySearchTree(50)
# for _ in range(15):
#     ele = random.randint(0, 100)
#     print("Inserting "+str(ele)+":")
#     BST.insert(ele)
#     # We have hidden the code for this function but it is available for use!
#     display(BST.root)
#     print('\n')
# BST = BinarySearchTree(6)
# lst = [4,9,5,2,8,12,10,14]
# for val in lst:
#     # print("Inserting " +str(val)+":")
#     BST.insert(val)
#     # display(BST.root)
#     # print('\n')
# display(BST.root)
# print(BST.search(9))
# print(BST.search(11))
BST = BinarySearchTree(6)
BST.insert(3)
BST.insert(2)
BST.insert(4)
BST.insert(-1)
BST.insert(1)
BST.insert(-2)
BST.insert(8)
BST.insert(7)

print("before deletion:")
display(BST.root)

BST.delete(6)
print("after deletion:")
display(BST.root)