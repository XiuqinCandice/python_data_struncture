def remove_edge(graph, source, destination):
    if graph.V == 0:
        return graph

    if source >= graph.V or source < 0 or destination >= graph.V or destination < 0:
        return graph
    
    prev = None
    current = graph.graph[source]
    # if the head node itself holds the key to be deleted
    if current is None:
        return
    if current is not None:    
        if current.vertex == destination:
            graph.graph[source] = current.next
            current.next = None
            return

    while current is not None:
        
        if current.vertex == destination:
            prev.next = current.next
            current.next = None
        
        prev = current
        current = current.next