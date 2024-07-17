def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col):
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    
    # Check the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    
    # Check the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    
    return True

def solve_n_queens(board, row):
    if row == len(board):
        print_board(board)
        return True
    
    result = False
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            result = solve_n_queens(board, row + 1) or result
            board[row][col] = '.'
    
    return result

def solve():
    N = 8
    board = [['.' for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("No solution exists")

if __name__ == "__main__":
    solve()
