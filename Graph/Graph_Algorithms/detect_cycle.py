from graph import Graph
def detect_cycle(graph):
    """
    Detects a cycle in a given graph
    :param graph: The graph
    :return: True if there is a cycle in the given graph, otherwise False
    """

    # visited list to keep track of the nodes that have been visited since the beginning of the algorithm
    visited = [False] * graph.V

    # stack keeps track of the nodes which are part of the current recursive call
    my_stack = [False] * graph.V

    for node in range(graph.V):
        # DFS 
        if detect_cycle_recursive(graph, node, visited, my_stack):
            return True

    return False


def detect_cycle_recursive(graph, node, visited, my_stack):
    """
    Detects a cycle in a given graph
    :param graph: The graph
    :param node: A source vertex
    :param visited: A list to track visited nodes
    :param stack: A helper stack
    :return: True if there is a cycle in the given graph, otherwise False
    """

    # Node was already in recursion stack. Cycle found.
    if my_stack[node]:
        return True

    # It has been visited before this recursion, 
    # or you have visited it before, the possibilities are checked, you are sure to return False since you have traversed through it
    if visited[node]:
        return False
    # Mark current node as visited and
    # add to recursion stack
    visited[node] = True
    my_stack[node] = True

    head = graph.graph[node]
    while head is not None:
        # Pick adjacent node and call it recursively
        adjacent = head.vertex
        # If the node is visited again in the same recursion => Cycle found
        if detect_cycle_recursive(graph, adjacent, visited, my_stack):
            return True
        head = head.next

    # remove the node from the recursive call
    my_stack[node] = False
    return False

# Main program to test the above code
if __name__ == "__main__":

    g1 = Graph(5)
    g1.add_edge(0, 1)
    g1.add_edge(0, 3)
    g1.add_edge(1, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 4)
    g1.add_edge(4, 1)

    g2 = Graph(3)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)

    print(detect_cycle(g1))
    print(detect_cycle(g2))