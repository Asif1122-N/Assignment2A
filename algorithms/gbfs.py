from node import SearchNode
from utils import heuristic
from utils import reconstruct_path

def gbfs(graph):
    visited = set()
    frontier = []
    origin = SearchNode(state=graph.origin)

    # Recursive function to perform greedy best-first search
    def expand(node):
        visited.add(node.state)

        if graph.is_goal(node.state):
            return node.state, len(visited), reconstruct_path(node)

        for neighbor_id, cost in graph.get_neighbors(node.state):
            if neighbor_id not in visited:
                child = SearchNode(state=neighbor_id, parent=node, cost=node.cost + cost, depth=node.depth + 1)
                
                frontier.append(child)
        
        # Sort the frontier by the heuristic cost
        frontier.sort(key=lambda x: min( heuristic(graph.nodes[dest], graph.nodes[x.state]) for dest in graph.destinations ))

        # Expand the node with the lowest heuristic cost
        if frontier:
            child = frontier.pop(0)
            result = expand(child)
            if result is not None:
                return result
            
    result = expand(origin)
    if result is not None:
        return result

    return None, None, []