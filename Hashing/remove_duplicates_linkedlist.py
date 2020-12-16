# def remove_duplicates(lst):
#     nodes_dict = {}
#     current_node = lst.get_head()
#     while current_node:
#         if current_node.next_element:
#             if current_node.next_element.data in nodes_dict:
#                 current_node.next_element = current_node.next_element.next_element
#             else:
#                 nodes_dict[current_node.data] = 0
#                 current_node = current_node.next_element
#         else:
#             current_node = current_node.next_element
#     return lst
def remove_duplicates(lst):
    current = lst.get_head()
    prev = lst.get_head()
    visited = set()
    while current:
        if current.data in visited:
            prev.next_element = current.next_element
            current = current.next_element
        else:
                visited.add(current.data)
                prev = current
                current = current.next_element

    return lst