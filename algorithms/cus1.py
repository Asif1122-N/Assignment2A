from node import SearchNode
from utils import reconstruct_path



def dls(node, graph, limit, generated_nodes):
    # Goal test
    if graph.is_goal(node.state):
        return node, generated_nodes
    
    # Depth limit reached
    if node.depth == limit:
        return None, generated_nodes
    
    # Expand in deterministic order
    neighbors = sorted(graph.get_neighbors(node.state), key = lambda x: x[0])

    for neighbor_id, cost in neighbors:

        child = SearchNode(
            state = neighbor_id,
            parent = node,
            cost = node.cost + cost,
            depth = node.depth + 1
        )

        generated_nodes += 1

        result, generated_nodes = dls(child, graph, limit, generated_nodes)

        if result is not None:
            return result, generated_nodes

    return None, generated_nodes

def cus1(graph):
    origin = graph.origin

    generated_nodes = 1
    depth_limit = 0

    while True:
        root = SearchNode(state = origin, cost = 0, depth = 0)

        result, generated_nodes = dls(root, graph, depth_limit, generated_nodes)

        if result is not None:
            return result.state, generated_nodes, reconstruct_path(result)
        
        depth_limit += 1

