from parser import parse_file
from graph import Graph

nodes, edges, origin, destinations = parse_file("test_cases/test1.txt")
graph = Graph(nodes, edges, origin, destinations)

from node import SearchNode

start = SearchNode(state=2)
child = SearchNode(state=3, parent=start, cost=4, depth=1)

print("Start state:", start.state)
print("Child state:", child.state)
print("Child parent:", child.parent.state)
print("Child cost:", child.cost)
print("Child depth:", child.depth)