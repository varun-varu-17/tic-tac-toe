import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if there is a winner
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full (i.e., a draw)
def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Function to make the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row = move // 3
            col = move % 3
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell is already occupied, try again!")
        except (ValueError, IndexError):
            print("Invalid move, try again!")

# Function to make the AI move using Minimax Algorithm
def ai_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # AI is 'O'
                score = minimax(board, False)
                board[i][j] = ' '  # Undo the move
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Minimax algorithm to evaluate moves
def minimax(board, is_maximizing):
    if check_win(board, 'O'):
        return 1
    elif check_win(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # AI is 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Human is 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '  # Undo the move
                    best_score = min(score, best_score)
        return best_score

# Main function to control the game
def tic_tac_toe():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    # Choose whether to go first or let AI go first
    first = input("Do you want to go first? (y/n): ").lower() == 'y'

    while True:
        print_board(board)
        
        if first:
            player_move(board)
            if check_win(board, 'X'):
                print_board(board)
                print("Player wins!")
                break
            first = False
        else:
            ai_move(board)
            if check_win(board, 'O'):
                print_board(board)
                print("AI wins!")
                break
            first = True

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    tic_tac_toe()
