G = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': [],
    'I': [],
}

# detect_cycle
# input: directed connected graph G = (V, E) with n vertices and m edges
# output: true if G contains a cycle, false otherwise


def detect_cycle(G, node, visited=set(), path=[]):
    visited.add(node)
    path += [node]

    for n in G[node]:
        if n not in visited:
            cycle = detect_cycle(G, n, visited, path)
            if cycle:
                return True
        elif n in path:
            return True

    return False


def main():
    print(detect_cycle(G, 'A'))


main()
