import sys
from parser import parse_file
from graph import Graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.gbfs import gbfs
from algorithms.astar import astar
from algorithms.cus1 import cus1
from algorithms.cus2 import cus2
import os

output_folder = "test_solution"

algorithms = ["DFS", "BFS", "GBFS", "AS", "CUS1", "CUS2"]

test_files = [
    "test_cases/test1.txt",
    "test_cases/test2.txt",
    "test_cases/test3.txt",
    "test_cases/test4.txt",
    "test_cases/test5.txt",
    "test_cases/test6.txt",
    "test_cases/test7.txt",
    "test_cases/test8.txt",
    "test_cases/test9.txt",
    "test_cases/test10.txt",
    "test_cases/test11.txt",
    "test_cases/test12.txt",
    "test_cases/test13.txt",
    "test_cases/test14.txt",
    "test_cases/test15.txt"
]

for test_file in test_files:

    node, edges, origin, destinations = parse_file(test_file)
    graph = Graph(node, edges, origin, destinations)
    base_name = test_file.split("/")[-1].replace(".txt", "")
    file_name = base_name + "_solution.txt"
    output_path = os.path.join(output_folder, file_name)

    with open(output_path, "w") as f:

        for algo in algorithms:

            if algo == "DFS":
                goal, n, path = dfs(graph)

            elif algo == "BFS":
                goal, n, path = bfs(graph)

            elif algo == "GBFS":
                goal, n, path = gbfs(graph)

            elif algo == "AS":
                goal, n, path = astar(graph)

            elif algo == "CUS1":
                goal, n, path = cus1(graph)

            elif algo == "CUS2":
                goal, n, path = cus2(graph)


            f.write(f"{test_file} {algo}\n")
            f.write(f"{goal} {n}\n")
            f.write("[" + ", ".join(map(str, path)) + "]\n\n")

