import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}
    
    def add_edge(self, u, v, weight):
        self.adjacency_list[u].append((v, weight))
        self.adjacency_list[v].append((u, weight))  # Assuming undirected graph
    
    def a_star(self, start, goal, heuristic):
        open_list = [(0, start)]  # (f_score, node)
        came_from = {}
        g_score = {vertex: float('inf') for vertex in self.vertices}
        g_score[start] = 0
        f_score = {vertex: float('inf') for vertex in self.vertices}
        f_score[start] = heuristic[start]

        while open_list:
            current_f, current = heapq.heappop(open_list)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            for neighbor, weight in self.adjacency_list[current]:
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return None  # No path found

# Example usage
if __name__ == "__main__":
    # Example graph initialization
    vertices = ['A', 'B', 'C', 'D', 'E']
    graph = Graph(vertices)
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 8)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('C', 'E', 4)
    graph.add_edge('D', 'E', 6)

    # Heuristic function (Manhattan distance to node E)
    heuristic = {
        'A': 8,
        'B': 5,
        'C': 4,
        'D': 2,
        'E': 0
    }

    start_node = 'A'
    goal_node = 'E'

    # Perform A* search
    path = graph.a_star(start_node, goal_node, heuristic)
    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
