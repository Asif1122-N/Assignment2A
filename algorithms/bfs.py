from collections import deque
from node import SearchNode
from utils import reconstruct_path


def bfs(graph):
    visited = set()
    frontier = deque()

    start_node = SearchNode(state=graph.origin)
    frontier.append(start_node)
    visited.add(start_node.state)

    nodes_created = 1

    while frontier:
        current_node = frontier.popleft()

        if graph.is_goal(current_node.state):
            return current_node.state, nodes_created, reconstruct_path(current_node)

        neighbors = sorted(graph.get_neighbors(current_node.state), key=lambda x: x[0])

        for neighbor_id, cost in neighbors:
            if neighbor_id not in visited:
                child_node = SearchNode(
                    state=neighbor_id,
                    parent=current_node,
                    cost=current_node.cost + cost,
                    depth=current_node.depth + 1
                )

                frontier.append(child_node)
                visited.add(neighbor_id)
                nodes_created += 1

    return None, nodes_created, []