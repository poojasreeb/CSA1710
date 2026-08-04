from itertools import permutations

def travelling_salesman(dist, start):
    cities = list(range(len(dist)))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for route in permutations(cities):
        cost = 0
        current = start

        for city in route:
            cost += dist[current][city]
            current = city

        cost += dist[current][start]

        if cost < min_cost:
            min_cost = cost
            best_path = [start] + list(route) + [start]

    return best_path, min_cost

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = travelling_salesman(distance, 0)

print("Shortest Path:", path)
print("Minimum Cost:", cost)
