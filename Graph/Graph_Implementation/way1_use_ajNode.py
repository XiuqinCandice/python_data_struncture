# A class to represent the adjacency list of the node
class AdjNode:

    def __init__(self, data):
        self.vertex = data
        self.next = None
    

class Graph:
    
    def __init__(self, vertices):
    # :param vertices: total number of vertices in a graph
        self.V = vertices # number of vertices
        self.graph = [None] * self.V
    
    # Function to add an edge in an undirected graph

    def add_edge(self, source, destination):
        '''
        :param source: source vertex (index in the list)
        :param destination: destination vertex
        '''

        # Add the destination node to the source node
        # implemente in a way similar to linkedlist that insert at head
        node = AdjNode(destination)
        node.next = self.graph[source] # connect destination node to the source
        self.graph[source] = node #after connection, set node as the source

        '''
        If is an undirected graph, add the source node to the destination 

        node = AdNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node
        '''
    
    def print_graph(self):

        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end = "")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end = "")
                temp = temp.next
            print("\n")


V = 5 # total number of vertices so initial list will be like [None,None,None,None,None]
g = Graph(V)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()