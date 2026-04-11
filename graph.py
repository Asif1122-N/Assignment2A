class Graph:
    def __init__(self, nodes, edges, origin, destinations):
        self.nodes = nodes
        self.edges = edges
        self.origin = origin
        self.destinations = destinations

        # Make sure every node has an edge list even if it has no outgoing edges
        for node_id in self.nodes:
            if node_id not in self.edges:
                self.edges[node_id] = []

    def get_neighbors(self, node_id):
        return self.edges[node_id]

    def is_goal(self, node_id):
        return node_id in self.destinations