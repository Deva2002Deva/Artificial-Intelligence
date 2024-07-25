def print_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}\n")

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # center column
        (2, 5, 8),  # right column
        (0, 4, 8),  # diagonal
        (2, 4, 6)   # other diagonal
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def play_game():
    board = [' '] * 9
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        try:
            move = int(input("Enter a position (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move. Position must be between 1 and 9.")
                continue
            if board[move] != ' ':
                print("Invalid move. Cell already taken.")
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
