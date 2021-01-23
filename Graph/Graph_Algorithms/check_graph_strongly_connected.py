from transpose_graph import transpose
from depth_first_traversal import dfs
# you can use either breadth first search or depth first search
def is_strongly_connected(graph):

    if len(dfs(graph, 0)) != graph.V:
        return False

    transposed_graph = transpose(graph)  


    if len(dfs(transposed_graph,0) ) != transposed_graph.V:
        return False
    
    return True


