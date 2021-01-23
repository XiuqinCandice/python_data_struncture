from graph import Graph
import copy
def connected_components(graph):
    visited = [False] * graph.V
    result = []
    for v in range(graph.V):
        if not visited[v]:
            result.append(dfs(graph, v, visited))
    return result


def dfs(g, source, visited):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return: returns the traversal in a string
    """

    graph = copy.deepcopy(g)

    # Create a stack for DFS
    stack = []

    # Result string
    result = ""

    # Push the source
    stack.append(source)

    while stack:

        # Pop a vertex from stack
        source = stack[-1]
        stack.pop()

        if not visited[source]:
            result += str(source)
            visited[source] = True

        # Get all adjacent vertices of the popped vertex source.
        # If a adjacent has not been visited, then push it
        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
            graph.graph[source] = graph.graph[source].next

    return result


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
result = connected_components(g)
print(result)