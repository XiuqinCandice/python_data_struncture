
from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):

    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    unique = set()
    result = LinkedList()

    start = list1.get_head()

    while start:
        unique.add(start.data)
        start = start.next_element

    start = list2.get_head()

    while start:
        unique.add(start.data)
        start = start.next_element

    for x in unique:
        result.insert_at_head(x)
        
    return result


# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    if (list1.is_empty()) or (list2.is_empty()):
        return None
    result = LinkedList()
    set1 = set()
    set2 = set()
    inter_set = set()
    start = list1.get_head()
    while start:
        set1.add(start.data)
        start = start.next_element

    start = list2.get_head()
    while start:
        set2.add(start.data)
        start = start.next_element

    inter_set = set1-(set1-set2)
    for x in inter_set:
        result.insert_at_head(x)
    return result


# def intersection(list1, list2):
#     if (list1.is_empty()) or (list2.is_empty()):
#         return None
#     result = LinkedList()
#     set1 = set()
#     set2 = set()
#     inter_set = set()
#     start = list1.get_head()
#     while start:
#         set1.add(start.data)
#         start = start.next_element

#     start = list2.get_head()
#     while start:
#         set2.add(start.data)
#         start = start.next_element

#     if len(set1) >= len(set2):
#         inter_set = set1-(set1-set2)
#     else:
#         inter_set = set2-(set2-set1)
#     for x in inter_set:
#         result.insert_at_head(x)
#     return result


