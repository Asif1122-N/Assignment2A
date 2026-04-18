from node import SearchNode
from utils import heuristic
from utils import reconstruct_path

# Custom 2 Algorithm: Combined Uniform Cost Search and Greedy Best-First Search ( Inspired by A* Search )
#Incorporates heuristic distance, costs of paths and depth to perform informed search

def cus2(graph):
    visited = set()
    frontier = []
    origin = SearchNode(state=graph.origin)

    nodes_created = 1

    def evaluation(node):
        closest_goal_distance = min(
        heuristic(graph.nodes[dest], graph.nodes[node.state])
        for dest in graph.destinations
        )
        # Incorporate depth into the evaluation
        return closest_goal_distance + (0.5 * node.cost) + (0.1 * node.depth)

    def expand(node):
        nonlocal nodes_created

        visited.add(node.state)
        #stops the search if we have reached a goal set
        if graph.is_goal(node.state):
            return node.state, nodes_created, reconstruct_path(node)

        neighbors = sorted(graph.get_neighbors(node.state), key=lambda x: x[0])

        for neighbor_id, cost in neighbors:
            if neighbor_id not in visited:
                child = SearchNode(
                    state=neighbor_id,
                    parent=node,
                    cost=node.cost + cost,
                    depth=node.depth + 1
                )
                frontier.append(child)
                nodes_created += 1

        frontier.sort(key=lambda x: (evaluation(x), x.state))

        while frontier:
            next_node = frontier.pop(0)
            # debugging print statement to show the node during search
            # print(f"Expanding node {next_node.state} with cost {next_node.cost} and depth {next_node.depth}")
            if next_node.state not in visited:
                result = expand(next_node)
                if result is not None:
                    return result

        return None

    result = expand(origin)

    if result is not None:
        return result
    # output a failed search result with the number of nodes created and a blank path
    return None, nodes_created, []
