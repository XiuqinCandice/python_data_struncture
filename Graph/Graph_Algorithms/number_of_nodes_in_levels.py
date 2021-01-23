# solution 1
from graph import Graph
def number_of_nodes(my_graph, level):

    queue = []
    visited = [0] * len(my_graph.graph)
# determine source, or a starting vertex
    for i in range(len(my_graph.graph)):
        if my_graph.graph[i] is not None:
            source = i

    queue.append(source)
    visited[source] = 1

    while queue:
        source = queue.pop(0)
        temp = my_graph.graph[source]
        while temp:
            vertex = temp.vertex
            if visited[vertex] == 0:
                queue.append(vertex)
                visited[vertex] = visited[source] + 1 # kid level is the parent level plus 1
            temp = temp.next
    
    # the number in the visited list are levels
    result = 0
    for num in visited:
        if num == level:
            result += 1
    
    return result


