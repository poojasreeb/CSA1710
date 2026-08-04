def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve(board, row + 1, n):
                return True
            board[row] = -1

    return False

n = int(input("Enter the value of N: "))
board = [-1] * n

if solve(board, 0, n):
    print("Solution Exists:\n")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No Solution Exists")
