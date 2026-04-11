def parse_file(filename):
    nodes = {}
    edges = {}
    origin = None
    destinations = set()

    section = None

    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("Nodes:"):
            section = "nodes"
            continue
        elif line.startswith("Edges:"):
            section = "edges"
            continue
        elif line.startswith("Origin:"):
            section = "origin"
            continue
        elif line.startswith("Destinations:"):
            section = "destinations"
            continue

        if section == "nodes":
            node_id, coords = line.split(":")
            node_id = int(node_id.strip())

            coords = coords.strip().replace("(", "").replace(")", "")
            x, y = map(int, coords.split(","))

            nodes[node_id] = (x, y)

        elif section == "edges":
            edge_part, cost = line.split(":")
            cost = int(cost.strip())

            edge_part = edge_part.strip().replace("(", "").replace(")", "")
            start, end = map(int, edge_part.split(","))

            if start not in edges:
                edges[start] = []

            edges[start].append((end, cost))

        elif section == "origin":
            origin = int(line)

        elif section == "destinations":
            parts = line.split(";")
            for part in parts:
                destinations.add(int(part.strip()))

    return nodes, edges, origin, destinations
