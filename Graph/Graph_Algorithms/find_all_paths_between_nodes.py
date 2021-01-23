from copy import deepcopy
from graph import Graph
def find_all_paths_helper(graph, source, destination, path, paths, visited):

    path.append(source)
    visited[source] = True

    if source == destination:
        paths.append(deepcopy(path))
    
    else:
        while graph.graph[source] is not None:
            vertex = graph.graph[source].vertex

            if not visited[vertex]:
                find_all_paths_helper(graph, vertex, destination, path, paths, visited)

            graph.graph[source] = graph.graph[source].next
    
    path.pop()
    visited[source] = False



def find_all_paths(graph, source, destination):
    path = []
    paths = []
    visited = [False] * len(graph.graph)
    find_all_paths_helper(graph, source, destination, path, paths, visited)
    return paths


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(2, 5)

source = 0
destination = 5

paths = find_all_paths(g, source, destination)
print(paths)