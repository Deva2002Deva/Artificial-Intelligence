import math

# Define the board size
BOARD_SIZE = 3

def print_board(board):
    for i in range(BOARD_SIZE):
        print(' | '.join(board[i * BOARD_SIZE:(i + 1) * BOARD_SIZE]))
        if i < BOARD_SIZE - 1:
            print('-' * (BOARD_SIZE * 4 - 1))
    print()

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Center column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal \
        (2, 4, 6)   # Diagonal /
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(BOARD_SIZE * BOARD_SIZE):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(BOARD_SIZE * BOARD_SIZE):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_move = -1
    best_score = -math.inf
    for i in range(BOARD_SIZE * BOARD_SIZE):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def play_game():
    board = [' '] * (BOARD_SIZE * BOARD_SIZE)
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        
        if player == 'X':
            move = find_best_move(board)
            print(f"Player {player} chooses position {move + 1}.")
        else:
            try:
                move = int(input("Enter a position (1-9): ")) - 1
                if move < 0 or move >= BOARD_SIZE * BOARD_SIZE or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

        board[move] = player
        
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        turn += 1

if __name__ == "__main__":
    play_game()
