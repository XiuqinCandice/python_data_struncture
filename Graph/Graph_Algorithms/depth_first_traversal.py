# when you append, you set it to True
# when you pop, you append it to the results
def dfs(my_graph, source):
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



# way 2 similar to bfs
def dfs(my_graph, source):

    visited = [False] * my_graph.V
    result = ""
    stack = []

    stack.append(source)
    visited[source] = True

    while stack:
        current = stack.pop()
        result += str(current)

        temp = my_graph.graph[current]
        while temp is not None:
            vertex = temp.vertex
            if visited[vertex] is False:
                stack.append(vertex)
                visited[vertex] = True
            temp = temp.next
    return result