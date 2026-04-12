from node import SearchNode

def dfs(graph):
    visited = set()
    path = []
    origin = SearchNode(state=graph.origin)
    
    # Recursive function to perform DFS.
    def expand(node):
        visited.add(node.state)
        path.append(node.state)

        if graph.is_goal(node.state):
            return node.state, node.depth, path

        for neighbor_id, cost in graph.get_neighbors(node.state):
            if neighbor_id not in visited:
                child = SearchNode(state=neighbor_id, parent=node, cost=node.cost + cost, depth=node.depth + 1)
                result = expand(child)
                if result is not None:
                    return result

        path.pop()
        return None


    result = expand(origin)
    if result is not None:
        return result

    return None, None, path

