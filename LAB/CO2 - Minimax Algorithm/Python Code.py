# Connect Four using Minimax Algorithm

ROWS = 6
COLS = 7

HUMAN = "X"
AI = "O"
EMPTY = "."

def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    print()
    for row in board:
        print(" ".join(row))
    print("0 1 2 3 4 5 6")


def is_valid_move(board, col):
    return board[0][col] == EMPTY


def get_valid_moves(board):
    return [col for col in range(COLS) if is_valid_move(board, col)]


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def get_next_row(board, col):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            return row
    return -1


def winning_move(board, piece):

    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col+i] == piece for i in range(4)):
                return True

    # Vertical
    for row in range(ROWS - 3):
        for col in range(COLS):
            if all(board[row+i][col] == piece for i in range(4)):
                return True

    # Positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True

    # Negative diagonal
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True

    return False


def evaluate_window(window):
    score = 0

    if window.count(AI) == 4:
        score += 100

    elif window.count(AI) == 3 and window.count(EMPTY) == 1:
        score += 5

    elif window.count(AI) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(HUMAN) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board):

    score = 0

    # Center column preference
    center = [board[row][COLS // 2] for row in range(ROWS)]
    score += center.count(AI) * 3

    # Horizontal
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = board[row][col:col+4]
            score += evaluate_window(window)

    # Vertical
    for col in range(COLS):
        for row in range(ROWS - 3):
            window = [board[row+i][col] for i in range(4)]
            score += evaluate_window(window)

    # Positive diagonal
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row+i][col+i] for i in range(4)]
            score += evaluate_window(window)

    # Negative diagonal
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row-i][col+i] for i in range(4)]
            score += evaluate_window(window)

    return score


def minimax(board, depth, maximizing_player):

    valid_moves = get_valid_moves(board)

    if winning_move(board, AI):
        return None, 1000000

    if winning_move(board, HUMAN):
        return None, -1000000

    if len(valid_moves) == 0:
        return None, 0

    if depth == 0:
        return None, score_position(board)

    if maximizing_player:
        best_score = -float("inf")
        best_col = valid_moves[0]

        for col in valid_moves:
            row = get_next_row(board, col)
            board[row][col] = AI

            score = minimax(board, depth - 1, False)[1]

            board[row][col] = EMPTY

            if score > best_score:
                best_score = score
                best_col = col

        return best_col, best_score

    else:
        best_score = float("inf")
        best_col = valid_moves[0]

        for col in valid_moves:
            row = get_next_row(board, col)
            board[row][col] = HUMAN

            score = minimax(board, depth - 1, True)[1]

            board[row][col] = EMPTY

            if score < best_score:
                best_score = score
                best_col = col

        return best_col, best_score


# Main Game
board = create_board()

print("CONNECT FOUR")
print("You = X")
print("Computer = O")

game_over = False

while not game_over:

    print_board(board)

    # Human move
    try:
        col = int(input("Enter column (0-6): "))

        if col not in range(COLS) or not is_valid_move(board, col):
            print("Invalid column!")
            continue

        row = get_next_row(board, col)
        drop_piece(board, row, col, HUMAN)

        if winning_move(board, HUMAN):
            print_board(board)
            print("You win!")
            break

    except ValueError:
        print("Enter a valid number!")
        continue

    if len(get_valid_moves(board)) == 0:
        print_board(board)
        print("Game Draw!")
        break

    # Computer move using Minimax
    col, score = minimax(board, 4, True)

    row = get_next_row(board, col)
    drop_piece(board, row, col, AI)

    print("Computer chooses column:", col)

    if winning_move(board, AI):
        print_board(board)
        print("Computer wins!")
        break
