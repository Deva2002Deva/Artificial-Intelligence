import math
from collections import deque

def is_solvable(capacity1, capacity2, target):
    return target % math.gcd(capacity1, capacity2) == 0

def water_jug_solver(capacity1, capacity2, target):
    if target > max(capacity1, capacity2):
        return "No solution"

    if not is_solvable(capacity1, capacity2, target):
        return "No solution"
    
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty
    path = []

    while queue:
        state = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        path.append(state)

        (jug1, jug2) = state
        if jug1 == target or jug2 == target:
            return path

        # Possible states to move to
        possible_states = [
            (capacity1, jug2),  # Fill jug1
            (jug1, capacity2),  # Fill jug2
            (0, jug2),          # Empty jug1
            (jug1, 0),          # Empty jug2
            (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2)),  # Pour jug1 to jug2
            (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1))   # Pour jug2 to jug1
        ]

        for next_state in possible_states:
            if next_state not in visited:
                queue.append(next_state)
    return "No solution"

capacity1 = 4
capacity2 = 3
target = 2

solution = water_jug_solver(capacity1, capacity2, target)
print(solution)
