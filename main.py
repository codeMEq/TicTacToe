# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        display_board()

        # Get the player's move
        valid_move = False
        while not valid_move:
            position = int(input("Enter your move (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == ' ':
                valid_move = True
            else:
                print("Invalid move. Try again.")

        # Update the board
        board[position] = current_player

        # Check if the current player has won
        if check_win(current_player):
            display_board()
            print("Player", current_player, "wins!")
            game_over = True
        # Check if it's a tie (board is full)
        elif ' ' not in board:
            display_board()
            print("It's a tie!")
            game_over = True
        # Switch to the next player
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
