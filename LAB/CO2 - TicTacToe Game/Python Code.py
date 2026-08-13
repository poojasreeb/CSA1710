# Tic-Tac-Toe Game

board = [" "] * 9

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def game():
    player = "X"

    for turn in range(9):
        display_board()

        while True:
            try:
                position = int(input(
                    f"Player {player}, enter position (1-9): "
                ))

                if position < 1 or position > 9:
                    print("Enter a number between 1 and 9.")
                elif board[position - 1] != " ":
                    print("Position already occupied.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        board[position - 1] = player

        if check_winner(player):
            display_board()
            print(f"Player {player} wins!")
            return

        player = "O" if player == "X" else "X"

    display_board()
    print("The game is a draw!")

game()
