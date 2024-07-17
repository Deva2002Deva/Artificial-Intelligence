from collections import deque

def bfs(graph, start):
    # Initialize a queue with the starting node
    queue = deque([start])
    # Set of visited nodes to prevent re-processing
    visited = set([start])
    # List to store the order of nodes visited
    bfs_order = []

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()
        bfs_order.append(vertex)

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                # Mark the neighbor as visited and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

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
print(f"BFS traversal starting from node {start_node}:")
bfs_order = bfs(graph, start_node)
print(bfs_order)
