from Graph import Graph

# Creating the graph with the values we needed
romania_map = Graph()
romania_map.add_edge('Arad', 'Sibiu', 140)
romania_map.add_edge('Arad', 'Timisoara', 118)
romania_map.add_edge('Arad', 'Zerind', 75)
romania_map.add_edge('Bucharest', 'Fagaras', 211)
romania_map.add_edge('Bucharest', 'Giurgiu', 90)
romania_map.add_edge('Bucharest', 'Pitesti', 101)
romania_map.add_edge('Bucharest', 'Urziceni', 85)
romania_map.add_edge('Craiova', 'Drobeta', 120)
romania_map.add_edge('Craiova', 'Pitesti', 138)
romania_map.add_edge('Craiova', 'Rimnicu', 146)
romania_map.add_edge('Drobeta', 'Mehadia', 75)
romania_map.add_edge('Eforie', 'Hirsova', 86)
romania_map.add_edge('Fagaras', 'Sibiu', 99)
romania_map.add_edge('Hirsova', 'Urziceni', 98)
romania_map.add_edge('Iasi', 'Neamt', 87)
romania_map.add_edge('Iasi', 'Vaslui', 140)
romania_map.add_edge('Lugoj', 'Mehadia', 70)
romania_map.add_edge('Lugoj', 'Timisoara', 111)
romania_map.add_edge('Oradea', 'Sibiu', 151)
romania_map.add_edge('Oradea', 'Zerind', 71)
romania_map.add_edge('Pitesti', 'Rimnicu', 97)
romania_map.add_edge('Rimnicu','Sibiu', 80)
romania_map.add_edge('Urziceni', 'Vaslui', 97)

# City coordinates taken from Mr. Badica laboratories
coordinates = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

def P1_task(path1, path2):
    print("Friend 1 is in " + path1[0])
    print("Friend 2 is in " + path2[0], '\n')

    # Both paths have the same lenght
    for i in range(0, len(path1) - 1):
        # They are in the same city
        if path1[i] == path2[i]:
            print("They have arrived in the same city")
            break

        # They are one city apart from each other
        if path1[i] == path2[i + 1]:
            print("Friend 2 goes to " + path2[i + 1])
            print("They have arrived in the same city")
            break

        if romania_map.get(path1[i], path1[i + 1]) > romania_map.get(path2[i], path2[i + 1]):
            print("Friend 2 arrives first in " + path2[i + 1] + " and waits")
            print("Friend 1 arrives in " + path1[i + 1])
        else:
            print("Friend 1 arrives first in " + path1[i + 1] + " and waits")
            print("Friend 2 arrives in " + path2[i + 1])
        print()