# Map Coloring using Constraint Satisfaction Problem (CSP)

colors = ["Red", "Green", "Blue"]

# Map of neighboring regions
neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

assignment = {}


def is_safe(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def backtracking():
    # If all regions are colored
    if len(assignment) == len(neighbors):
        return True

    # Select an unassigned region
    for region in neighbors:
        if region not in assignment:
            break

    # Try each color
    for color in colors:
        if is_safe(region, color):
            assignment[region] = color

            if backtracking():
                return True

            # Backtrack
            del assignment[region]

    return False


# Start CSP solving
if backtracking():
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, "->", color)
else:
    print("No solution exists.")
