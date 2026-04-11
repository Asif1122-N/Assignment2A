from parser import parse_file

nodes, edges, origin, destinations = parse_file("test_cases/test1.txt")

print("Nodes:", nodes)
print("Edges:", edges)
print("Origin:", origin)
print("Destinations:", destinations)