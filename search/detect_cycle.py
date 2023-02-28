G = {
    'A': ['B', 'G'],
    'B': ['C', 'D', 'E'],
    'C': [],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['G'],
    'I': [],
}


def detect_cycle(G, node):
    visited = []
    stack = []
    cycle = False

    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()

        for n in reversed(G[s]):
            if n in visited:
                cycle = True
                break
            elif n not in visited:
                visited.append(n)
                stack.append(n)

    return cycle


def main():
    print(detect_cycle(G, 'A'))


main()
