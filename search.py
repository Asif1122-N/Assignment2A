import sys

from parser import parse_file
from graph import Graph

# Try argument 1 from the command-line arguments and assign it to input_file.
try:
    input_file = sys.argv[1]
except IndexError:
    # Default to test1.txt if no argument is provided.
    input_file = "test_cases/test1.txt"

nodes, edges, origin, destinations = parse_file(input_file)
graph = Graph(nodes, edges, origin, destinations)

# Try argument 2 from the command-line arguments and assign it to search_algorithm.
try:
    search_algorithm = sys.argv[2]
except IndexError:
    # Default to dfs if no argument is provided.
    search_algorithm = "DFS"

from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.gbfs import gbfs
from algorithms.astar import astar
from algorithms.cus1 import cus1
from algorithms.cus2 import cus2

# Selects the search algorithm
if search_algorithm == "BFS":
    goal, number_of_nodes, path = bfs(graph)

elif search_algorithm == "DFS":
    goal, number_of_nodes, path = dfs(graph)

elif search_algorithm == "GBFS":
    goal, number_of_nodes, path = gbfs(graph)

elif search_algorithm == "AS":
    goal, number_of_nodes, path = astar(graph)

elif search_algorithm == "CUS1":
    goal, number_of_nodes, path = cus1(graph)

elif search_algorithm == "CUS2":
    goal, number_of_nodes, path = cus2(graph)

# Print the results
if goal is None:
    print("No solution found.")
else:
    print("## Test: " + f"{input_file}" + " - Method: " + f"{search_algorithm}")
    print(f"{input_file} {search_algorithm}")
    print(f"{goal} {number_of_nodes}")
    print("[" + ", ".join(map(str, path)) + "]")

    # for i in range(len(path) - 1):
    #    if path[i] != goal:
    #        print(str(path[i]) + " -> " + str(path[i + 1]))
    #    else:
    #        print(str(path[i]))


# OLD TEST CODE
# start = SearchNode(state=2)
# child = SearchNode(state=3, parent=start, cost=4, depth=1)

# print("Start state:", start.state)
# print("Child state:", child.state)
# print("Child parent:", child.parent.state)
# print("Child cost:", child.cost)
# print("Child depth:", child.depth)
