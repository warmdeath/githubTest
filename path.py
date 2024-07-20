my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph,start,target=None):
    unvisited = list(graph)
    distances_from_start = {node:0 if node == start else float("inf") for node in unvisited}
    paths_from_start = {node:[] for node in unvisited}
    paths_from_start[start].append(start)
    
    while unvisited:
        current = min(unvisited,key=distances_from_start.get)

        for neighbour,distance in graph[current]:
            if distance + distances_from_start[current] < distances_from_start[neighbour]:
                distances_from_start[neighbour] = distance + distances_from_start[current]
                if paths_from_start[neighbour] and paths_from_start[neighbour][-1] == neighbour:
                    paths_from_start[neighbour] = paths_from_start[current][:]
                else:
                    paths_from_start[neighbour].extend(paths_from_start[current])
                paths_from_start[neighbour].append(neighbour)
        unvisited.remove(current)
        targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances_from_start[node]}\nPath: {" -> ".join(paths_from_start[node])}')
    return distances_from_start, paths_from_start

shortest_path(my_graph,"A")