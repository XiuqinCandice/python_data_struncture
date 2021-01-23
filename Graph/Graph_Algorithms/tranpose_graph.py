# make a graph same as the length of the given one and reverse it

# way 1 use add_edge function directly
from graph import Graph, AdjNode
def transpose(my_graph):

    new_graph = Graph(my_graph.V)

    for source in range(my_graph.V):
        while my_graph.graph[source] is not None:
            destination = my_graph.graph[source].vertex
            new_graph.add_edge(destination, source)
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph

# way 2 reverse edge direction directly
'''
def transpose(my_graph):

    new_graph = Graph(my_graph.V)

    for source in range(my_graph.V):
        # my_graph is the graph with nodes initially, new graph was empty
        while my_graph.graph[source] is not None:
            vertex = my_graph.graph[source].vertex
            # the source will become the node to be inserted at the vertex node
            node = AdjNode(source)
            node.next = new_graph.graph[vertex]
            new_graph.graph[vertex] = node
            my_graph.graph[source] = my_graph.graph[source].next

    return new_graph
'''