import heapq

class PuzzleState:
    def __init__(self, board, empty_tile_pos, cost=0, moves=0, prev_state=None):
        self.board = board
        self.empty_tile_pos = empty_tile_pos
        self.cost = cost
        self.moves = moves
        self.prev_state = prev_state

    def __lt__(self, other):
        return (self.cost + self.moves) < (other.cost + other.moves)

    def is_goal(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return self.board == goal

    def get_neighbors(self):
        neighbors = []
        x, y = self.empty_tile_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = self.board[:]
                new_board[x * 3 + y], new_board[new_x * 3 + new_y] = new_board[new_x * 3 + new_y], new_board[x * 3 + y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.cost, self.moves + 1, self))
        
        return neighbors

    def heuristic(self):
        goal_pos = [(i // 3, i % 3) for i in range(9)]
        total_distance = 0
        for i, tile in enumerate(self.board):
            if tile != 0:
                goal_x, goal_y = goal_pos[tile]
                curr_x, curr_y = i // 3, i % 3
                total_distance += abs(goal_x - curr_x) + abs(goal_y - curr_y)
        return total_distance

def solve_puzzle(initial_board):
    empty_tile_pos = initial_board.index(0)
    empty_tile_pos = (empty_tile_pos // 3, empty_tile_pos % 3)
    
    initial_state = PuzzleState(initial_board, empty_tile_pos)
    initial_state.cost = initial_state.heuristic()
    
    priority_queue = []
    heapq.heappush(priority_queue, initial_state)
    
    visited = set()
    visited.add(tuple(initial_board))
    
    while priority_queue:
        current_state = heapq.heappop(priority_queue)
        
        if current_state.is_goal():
            return current_state
        
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in visited:
                neighbor.cost = neighbor.heuristic()
                heapq.heappush(priority_queue, neighbor)
                visited.add(tuple(neighbor.board))
    
    return None

def print_solution(solution_state):
    if not solution_state:
        print("No solution found")
        return

    moves = []
    state = solution_state
    while state:
        moves.append(state.board)
        state = state.prev_state

    moves.reverse()
    for move in moves:
        print_board(move)
        print("")

def print_board(board):
    for i in range(3):
        print(board[3 * i: 3 * (i + 1)])

if __name__ == "__main__":
    initial_board = [1, 2, 3, 4, 0, 5, 6, 7, 8]
    solution_state = solve_puzzle(initial_board)
    print_solution(solution_state)
