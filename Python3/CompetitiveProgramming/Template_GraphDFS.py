class Graph:    # simple graph using adjacency lists
    V = 0   # number of vertices (0 to v - 1 vertices)
    ADJ = []    #adjacency list
    def __init__(self, v):
        self.V = v
        self.ADJ = [[] for _ in range(self.V)]

    def addEdge(self, i, j, undir = True):	# undirected graph
        self.ADJ[i].append(j)
        if undir:
            self.ADJ[j].append(i)

    def dfs(self, src):
        dfs_path = []
        visited = [False] * self.V
        def dfsUtil(node):
            dfs_path.append(node)
            visited[node] = True
            for nbr in self.ADJ[node]:
                if not visited[nbr]:
                    dfsUtil(nbr)
            return
        dfsUtil(src)
        print(*dfs_path)

    def printAdjList(self):
        for i in range(self.V):
            print("{} : {}".format(i, self.ADJ[i]))

def main():
    g = Graph(7)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(5, 6)
    g.addEdge(4, 5)
    g.addEdge(0, 4)
    g.addEdge(3, 4)
    g.dfs(1)

if __name__ == '__main__':
    main()
