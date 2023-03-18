# Using a Python dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K']
}


# function for dfs:
def recursive_dfs(graph, source, path=[]):
    if source not in path:
        path.append(source)
        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            path = recursive_dfs(graph, neighbour, path)
    return path


# Driver Code
path = recursive_dfs(graph, 'A')
print("DFS Graph traversal is given as:", " ".join(path))
