from Graph import Node, Graph
from Utils import add_to_open

def astar_search(graph, heuristics, src, dest):
    open = []
    explored = []

    # Create the start node and the goal node
    start = Node(src, None)
    goal = Node(dest, None)

    # Add the first node to the open list
    open.append(start)

    # Loop until the list is empty
    while len(open) > 0:
        # Keep the list sorted so we extract only the smallest element
        open.sort()

        # Get the node with the lowest cost
        current_node = open.pop(0)

        # Add the current node to the explored nodes list
        explored.append(current_node)

        # Check if the current node is the goal node
        # If we reached the goal, return the path
        if current_node == goal:
            # Store the path from destination node to the source node
            path = []
            while current_node != start:
                path.append(current_node.name)
                current_node = current_node.parent
            path.append(src)

            # Return reversed path
            return path[::-1]

        # Get neighbors
        neighbors = graph.get(current_node.name)

        # Loop through neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)

            # Check if the neighbor is in the closed list
            if(neighbor in explored):
                continue

            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics[neighbor.name]
            neighbor.f = neighbor.g + neighbor.h

            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)

    # Return None if no path is found
    return None