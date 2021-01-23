from graph import Graph
def bfs(my_graph, source):

    result = ""
    visited = [False] * len(my_graph.graph)
    queue = []

    queue.append(source)
    visited[source] = True

    while queue:
        current = queue.pop(0)
        result += str(current)

        temp = my_graph.graph[current]
        while temp is not None:
            vertex = temp.vertex
            if visited[vertex] is False:
                queue.append(vertex)
                visited[vertex] = True
            temp = temp.next
    return result
'''
The time complexity of BFS can be computed as the total number of iterations performed by the while loop in the code above.

Let EE be the set of all edges in the connected component visited by the algorithm. For each edge {u, v}u,v in EE the algorithm makes two while loop iteration steps: one time when the algorithm visits the neighbors of uu and one time when it visits the neighbors of vv.

Hence, the time complexity is O(∣V∣ +∣E∣).
'''


V = 5
g = Graph(V)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)

print(bfs(g, 0))


    