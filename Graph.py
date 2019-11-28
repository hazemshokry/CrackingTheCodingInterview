from collections import defaultdict


class Node(object):
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs_traversal(self, v):
        if v is None:
            return
        visited = [False for n in self.graph]
        self.dfs_helper(v, visited)

    def dfs_helper(self, v, visited=[]):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_helper(i, visited)


def dfs_traversal(g, u):
    if u is None:
        return
    visited = [False for i in g]
    dfs_helper(g, u, visited)


def dfs_helper(g, u, visited):
    visited[u] = True
    print(u)
    for v in g[u]:
        if visited[v] == False:
            dfs_helper(g, v, visited)




if __name__ == '__main__':
    g = {0: [1, 4, 5], 1: [3, 4], 2: [], 3: [2, 4], 4: [], 5: []}

    print(g)
    dfs_traversal(g, 0)
