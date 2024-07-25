def is_valid(coloring, graph, node, color):
    for neighbor in graph[node]:
        if coloring[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, coloring, node):
    if node == len(graph):
        return True

    for color in colors:
        if is_valid(coloring, graph, node, color):
            coloring[node] = color
            if map_coloring(graph, colors, coloring, node + 1):
                return True
            coloring[node] = None

    return False

def main():
    # Define the graph as an adjacency list
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 3],
        3: [0, 2]
    }

    # List of colors to use
    colors = ['Red', 'Green', 'Blue']

    # Initialize coloring
    coloring = [None] * len(graph)

    if map_coloring(graph, colors, coloring, 0):
        print("Solution found:", coloring)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
