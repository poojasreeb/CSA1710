from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m > 0 and m < c):
        return False
    if ((3 - m) > 0 and (3 - m) < (3 - c)):
        return False
    return True

def bfs():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')

    queue = deque([(start, [])])
    visited = set()

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        m, c, boat = state

        for dm, dc in moves:
            if boat == 'L':
                new = (m - dm, c - dc, 'R')
            else:
                new = (m + dm, c + dc, 'L')

            if is_valid(new[0], new[1]):
                queue.append((new, path + [state]))

    return None

solution = bfs()

if solution:
    print("Solution Path:")
    for s in solution:
        print(s)
else:
    print("No Solution Found")
