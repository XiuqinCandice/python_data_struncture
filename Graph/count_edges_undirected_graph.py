from Graph import Graph
# We only need Graph for this Question!


def num_edges(g):
    # For undirected graph, just sum up the size of
    # all the adjacency lists for each vertex
    sum = 0
    for i in range(g.vertices):
        sum += g.array[i].length()
        # temp = g.array[i].head_node
        # while (temp is not None):
        #     sum += 1
        #     temp = temp.next_element

    # Half the total sum as it is an undirected graph
    return sum//2


# or one line of code
# def num_edges(g):
    # return sum([g.array[i].length() for i in range(g.vertices)])//2

g = Graph(9)
g.add_edge(0, 2)
g.add_edge(0, 5)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(5, 3)
g.add_edge(5, 6)
g.add_edge(3, 6)
g.add_edge(6, 7)
g.add_edge(6, 8)
g.add_edge(6, 4)
g.add_edge(7, 8)



g2 = Graph(7)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(3, 4)
g2.add_edge(3, 5)
g2.add_edge(2, 5)
g2.add_edge(2, 4)
g2.add_edge(4, 6)
g2.add_edge(4, 5)
g2.add_edge(6, 5)


print(num_edges(g))

print(num_edges(g2))
