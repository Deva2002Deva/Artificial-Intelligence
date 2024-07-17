from collections import deque

def is_valid(state):
    m1, c1, m2, c2, boat = state
    if m1 < 0 or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    if m1 > 0 and m1 < c1:
        return False
    if m2 > 0 and m2 < c2:
        return False
    return True

def get_successors(state):
    m1, c1, m2, c2, boat = state
    successors = []
    if boat == 1:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m1 - m, c1 - c, m2 + m, c2 + c, 0)
            if is_valid(new_state):
                successors.append(new_state)
    else:
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (m1 + m, c1 + c, m2 - m, c2 - c, 1)
            if is_valid(new_state):
                successors.append(new_state)
    return successors

def solve_missionaries_cannibals():
    initial_state = (3, 3, 0, 0, 1)
    goal_state = (0, 0, 3, 3, 0)
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [goal_state]
        
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    return "No solution"

solution = solve_missionaries_cannibals()
print(solution)
