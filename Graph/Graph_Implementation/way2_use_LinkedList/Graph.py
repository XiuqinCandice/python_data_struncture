from LinkedList import LinkedList

class Graph:
    def __init__(self, vertices):
        # total number of vertices
        self.vertice = vertices
        self.array = []
        for i in range(self.vertices):
            temp = LinkedList()
            self.array.append(temp)
    
    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            self.array[source].insert_at_head(destination)
        # Uncomment the following line for undirected graph 
            # self.array[destination].insert_at_head(source)
    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end = " | => ")
            temp = self.array[i].get_head()
            while temp:
                print("[", temp.data, end = " ] -> ")
                temp = temp.next_element
            print("None")