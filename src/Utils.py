from math import sqrt

def distance(a,b):
    "Calculate Euclidian distance"
    x1,y1 = a
    x2,y2 = b
    return int(sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)))

def calculate_heuristics(dest, coordinates):
    """Get the heuristic (straight-line distance) values from each city coordinates.
    The values are from any city to the destination city."""
    heuristics = {}
    for city in coordinates:
        if city == dest:
            heuristics[city] = 0
        else:
            heuristics[city] = distance(coordinates[city],coordinates[dest])
    return heuristics

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

