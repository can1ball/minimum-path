from P1 import *
from Utils import calculate_heuristics
from Search import astar_search

def main():
    print("Choose city from list of possible cities:")
    print("Arad, Bucharest, Craiova, Drobeta, Eforie, Fagaras, Giuegiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea,")
    print("Pitesti, Rimnicu, Sibiu, Timisoara, Urziceni, Vaslui, Zerind", end='\n')
    city1 = input("Input the first city ")
    city2 = input("Input the second city ")

    heuristic = calculate_heuristics(city1, coordinates)

    path1 = astar_search(romania_map, heuristic, city1, city2)
    path2 = astar_search(romania_map, heuristic, city2, city1)

    P1_task(path1, path2)

# Example of an odd length path
def example1():
    city1 = 'Arad'
    city2 = 'Bucharest'

    heuristic = calculate_heuristics(city1, coordinates)

    path1 = astar_search(romania_map, heuristic, city1, city2)
    path2 = astar_search(romania_map, heuristic, city2, city1)

    P1_task(path1, path2)

# Example of an even length path
def example2():
    city1 = 'Arad'
    city2 = 'Craiova'

    heuristic = calculate_heuristics(city1, coordinates)

    path1 = astar_search(romania_map, heuristic, city1, city2)
    path2 = astar_search(romania_map, heuristic, city2, city1)

    P1_task(path1, path2)

if __name__ == "__main__":
    #main()
    #example1()
    example2()