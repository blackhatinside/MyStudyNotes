class Graph:    # simple graph using adjacency lists
    V = 0   # number of vertices (0 to v - 1 vertices)
    ADJ = []    #adjacency list
    def __init__(self, v):
        self.V = v
        self.ADJ = [[] for _ in range(self.V)]

    def addEdge(self, i, j, undir = True):
        self.ADJ[i].append(j)
        if undir:
            self.ADJ[j].append(i)

    def bfs(self, src, dest = -1):
        q = []
        bfs_path = []
        dist = [0] * self.V
        parent = [0] * self.V
        visited = [False] * self.V
        q.append(src)
        dist[src] = 0
        parent[src] = src
        visited[src] = True
        while q:
            x = q.pop(0)
            bfs_path.append(x)
            for nbr in self.ADJ[x]:
                if not visited[nbr]:
                    q.append(nbr)
                    dist[nbr] = dist[x] + 1
                    parent[nbr] = x
                    visited[nbr] = True
        print(*bfs_path)

        # single source shortest path for undirected graph
        # for i in range(self.V):   
        #     print("Shortest dist to {} is {}".format(i, dist[i]))

        if dest != -1:
            temp = dest
            bfs_path_s2d = []
            while temp != src:
                bfs_path_s2d.append(temp)
                temp = parent[temp]
            bfs_path_s2d.append(src)
            print(*bfs_path_s2d)

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
    g.bfs(1)

if __name__ == '__main__':
    main()
