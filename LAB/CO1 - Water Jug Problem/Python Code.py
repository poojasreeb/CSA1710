from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue
        visited.add((a, b))

        path = path + [(a, b)]

        if a == target or b == target:
            return path

        next_states = [
            (cap1, b),                      # Fill Jug 1
            (a, cap2),                      # Fill Jug 2
            (0, b),                         # Empty Jug 1
            (a, 0),                         # Empty Jug 2
            (a - min(a, cap2 - b), b + min(a, cap2 - b)),  # Pour Jug1 -> Jug2
            (a + min(b, cap1 - a), b - min(b, cap1 - a))   # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None

capacity1 = 4
capacity2 = 3
target = 2

solution = water_jug(capacity1, capacity2, target)

if solution:
    print("Solution Path:")
    for state in solution:
        print(state)
else:
    print("No Solution Exists")
