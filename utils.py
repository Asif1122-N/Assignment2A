def heuristic(destination, state):
    return abs(destination[0] - state[0]) + abs(destination[1] - state[1])

def reconstruct_path(node):
        path = []
        while node is not None:
            path.append(node.state)
            node = node.parent
        return list(reversed(path))