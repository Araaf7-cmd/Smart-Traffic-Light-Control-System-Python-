def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                if n not in visited and n not in queue:
                    queue.append(n)
    return visited


graph = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['i'],
    'd': [],
    'e': ['d', 'f'],
    'f': ['g'],
    'g': ['j'],
    'i': [],
    'j': ['k']
}

start_node = 'a'
print("BFS Traversal starting from", start_node, ":", bfs(graph, start_node))
