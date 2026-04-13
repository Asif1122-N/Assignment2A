from node import SearchNode
from utils import reconstruct_path

def dfs(graph):
    visited = set()
    origin = SearchNode(state=graph.origin)
    
    # Recursive function to perform DFS.
    def expand(node):
        visited.add(node.state)
        if graph.is_goal(node.state):
            return node.state, node.depth, reconstruct_path(node)

        for neighbor_id, cost in graph.get_neighbors(node.state):
            if neighbor_id not in visited:
                child = SearchNode(state=neighbor_id, parent=node, cost=node.cost + cost, depth=node.depth + 1)
                result = expand(child)
                if result is not None:
                    return result

        return None


    result = expand(origin)
    if result is not None:
        return result

    return None, None, []

