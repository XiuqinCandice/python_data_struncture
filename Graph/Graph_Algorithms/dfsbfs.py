
import copy
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
    
    def add_edge(self, s: int, d: int):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

def dfs_mark_visited_after_stack_append(my_graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a string
    """
    
    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack.pop()
        result += str(source)
        

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
                visited[source] = True
            my_graph.graph[source] = my_graph.graph[source].next

    return result

def dfs_mark_visited_after_result_append(my_graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a string
    """
    
    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack.pop()
        
        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            my_graph.graph[source] = my_graph.graph[source].next

    return result

def bfs_mark_visited_after_queue_append(my_graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    
    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a queue for BFS
    queue = []

    # Result string
    result = ""

    # Mark the source node as
    # visited and enqueue it
    queue.append(source)
    visited[source] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        source = queue.pop(0)
        result += str(source)

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                queue.append(data)
                visited[data] = True
            my_graph.graph[source] = my_graph.graph[source].next

    return result

def bfs_mark_visited_after_result_append(my_graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    
    # Mark all the vertices as not visited
    visited = [False] * (len(my_graph.graph))

    # Create a queue for BFS
    queue = []

    # Result string
    result = ""

    queue.append(source)

    while queue:

        # Dequeue a vertex from the queue
        source = queue.pop(0)

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the
        # dequeued vertex source. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        while my_graph.graph[source] is not None:
            data = my_graph.graph[source].vertex
            if not visited[data]:
                queue.append(data)
            my_graph.graph[source] = my_graph.graph[source].next

    return result

if __name__ == '__main__':
    my_graph = Graph(20)
    my_graph.add_edge(1, 2)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(3, 4)
    my_graph.add_edge(2, 5)

    assert(bfs_mark_visited_after_queue_append(copy.deepcopy(my_graph), 1) == bfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 1))
    assert(dfs_mark_visited_after_stack_append(copy.deepcopy(my_graph), 1) == dfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 1))
    assert(bfs_mark_visited_after_queue_append(copy.deepcopy(my_graph), 2) == bfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 2))
    assert(dfs_mark_visited_after_stack_append(copy.deepcopy(my_graph), 2) == dfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 2))
    assert(bfs_mark_visited_after_queue_append(copy.deepcopy(my_graph), 3) == bfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 3))
    assert(dfs_mark_visited_after_stack_append(copy.deepcopy(my_graph), 3) == dfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 3))
    assert(bfs_mark_visited_after_queue_append(copy.deepcopy(my_graph), 4) == bfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 4))
    assert(dfs_mark_visited_after_stack_append(copy.deepcopy(my_graph), 4) == dfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 4))
    assert(bfs_mark_visited_after_queue_append(copy.deepcopy(my_graph), 5) == bfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 5))
    assert(dfs_mark_visited_after_stack_append(copy.deepcopy(my_graph), 5) == dfs_mark_visited_after_result_append(copy.deepcopy(my_graph), 5))