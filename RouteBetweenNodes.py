# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

def route_between_nodes(graph, u, v):
    if u == None or v == None:
        return
    visited = [False for n in graph]
    route_between_nodes_helper(graph, u, v, visited)


def route_between_nodes_helper(graph, u, v, visited, path=[]):

    visited[u] = True
    path.append(u)

    if v in path:
        print(path)
        print(True)

    for i in graph[u]:
        if not visited[i]:
            route_between_nodes_helper(graph, i, v, visited, path)

    path.pop()

if __name__ == '__main__':
    g = {0: [1, 5, 4], 1: [4, 3], 2: [], 3: [2, 4], 4: [], 5: []}

    route_between_nodes(g, 1, 5)
