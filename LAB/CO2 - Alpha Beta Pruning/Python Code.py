# Tic-Tac-Toe using Alpha-Beta Pruning

HUMAN = "X"
AI = "O"
EMPTY = " "

board = [EMPTY] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

def is_draw():
    return EMPTY not in board

def minimax(alpha, beta, maximizing):
    if check_winner(AI):
        return 1

    if check_winner(HUMAN):
        return -1

    if is_draw():
        return 0

    if maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI

                score = minimax(alpha, beta, False)

                board[i] = EMPTY

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                # Alpha-Beta Pruning
                if alpha >= beta:
                    break

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN

                score = minimax(alpha, beta, True)

                board[i] = EMPTY

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                # Alpha-Beta Pruning
                if alpha >= beta:
                    break

        return best_score

def best_move():
    best_score = -float("inf")
    move = -1

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI

            score = minimax(-float("inf"), float("inf"), False)

            board[i] = EMPTY

            if score > best_score:
                best_score = score
                move = i

    return move

# Main game
print("TIC-TAC-TOE")
print("You = X")
print("Computer = O")

while True:
    display_board()

    # Human move
    try:
        position = int(input("Enter position (1-9): ")) - 1

        if position < 0 or position > 8 or board[position] != EMPTY:
            print("Invalid move!")
            continue

        board[position] = HUMAN

    except ValueError:
        print("Enter a valid number!")
        continue

    if check_winner(HUMAN):
        display_board()
        print("You win!")
        break

    if is_draw():
        display_board()
        print("Game Draw!")
        break

    # Computer move
    move = best_move()
    board[move] = AI

    print("Computer chooses position:", move + 1)

    if check_winner(AI):
        display_board()
        print("Computer wins!")
        break

    if is_draw():
        display_board()
        print("Game Draw!")
        break
