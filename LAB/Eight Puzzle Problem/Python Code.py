from collections import deque

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)

    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }

    for move in moves[zero]:
        new_state = list(state)
        new_state[zero], new_state[move] = new_state[move], new_state[zero]
        neighbors.append(tuple(new_state))

    return neighbors

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            queue.append((neighbor, path + [state]))

    return None

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = bfs(start, goal)

if solution:
    print("Solution Found:\n")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No Solution Exists")
