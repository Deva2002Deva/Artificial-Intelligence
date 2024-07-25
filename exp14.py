import math

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

def alpha_beta(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    if check_winner(board, 'O'):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(BOARD_SIZE * BOARD_SIZE):
            if board[i] == ' ':
                board[i] = 'X'
                eval = alpha_beta(board, depth + 1, alpha, beta, False)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE * BOARD_SIZE):
            if board[i] == ' ':
                board[i] = 'O'
                eval = alpha_beta(board, depth + 1, alpha, beta, True)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def find_best_move(board):
    best_move = -1
    best_value = -math.inf
    alpha = -math.inf
    beta = math.inf

    for i in range(BOARD_SIZE * BOARD_SIZE):
        if board[i] == ' ':
            board[i] = 'X'
            move_value = alpha_beta(board, 0, alpha, beta, False)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i
            alpha = max(alpha, move_value)
    
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
