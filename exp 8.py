from collections import deque

# BFS implementation
def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    bfs_order = []

    while queue:
        vertex = queue.popleft()
        bfs_order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

# DFS implementation (recursive)
def dfs_recursive(graph, start, visited=None, dfs_order=None):
    if visited is None:
        visited = set()
    if dfs_order is None:
        dfs_order = []

    visited.add(start)
    dfs_order.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, dfs_order)

    return dfs_order

# DFS implementation (iterative)
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()
    dfs_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            dfs_order.append(vertex)
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return dfs_order

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'

# Perform BFS
print(f"BFS traversal starting from node {start_node}:")
bfs_order = bfs(graph, start_node)
print(bfs_order)

# Perform DFS (recursive)
print(f"DFS (recursive) traversal starting from node {start_node}:")
dfs_order_recursive = dfs_recursive(graph, start_node)
print(dfs_order_recursive)

# Perform DFS (iterative)
print(f"DFS (iterative) traversal starting from node {start_node}:")
dfs_order_iterative = dfs_iterative(graph, start_node)
print(dfs_order_iterative)
