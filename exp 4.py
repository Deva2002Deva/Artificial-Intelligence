from itertools import permutations

def is_valid_solution(puzzle, solution_map):
    translated_puzzle = puzzle.translate(str.maketrans(solution_map))
    terms = translated_puzzle.split()
    num1, num2, result = int(terms[0]), int(terms[2]), int(terms[4])
    return num1 + num2 == result

def solve_cryptarithm(puzzle):
    letters = ''.join(set(filter(str.isalpha, puzzle)))
    digits = '0123456789'
    
    for perm in permutations(digits, len(letters)):
        solution_map = {letters[i]: perm[i] for i in range(len(letters))}
        if is_valid_solution(puzzle, solution_map):
            return solution_map
    return "No solution"

puzzle = "SEND + MORE = MONEY"
solution = solve_cryptarithm(puzzle)
if solution != "No solution":
    print('Solution:', solution)
    print(''.join([solution[char] if char in solution else char for char in puzzle]))
else:
    print(solution)
