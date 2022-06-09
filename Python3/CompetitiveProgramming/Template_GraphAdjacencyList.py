class Graph:    # complex graph using adjacency lists
    V = 0   # number of vertices (0 to v - 1 vertices)
    ADJ = []    #adjacency list
    def __init__(self, v):
        self.V = v
        self.ADJ = [[] for _ in range(self.V)]

    def addEdge(self, i, j, undir = True):
        self.ADJ[i].append(j)
        if undir:
            self.ADJ[j].append(i)

    def bfs(self, src):
        q = []
        visited = [False] * self.V
        q.append(src)
        visited[src] = True
        while q:
            x = q.pop(0)
            print(x, end = " ")
            for nbr in self.ADJ[x]:
                if not visited[nbr]:
                    q.append(nbr)
                    visited[nbr] = True

    def printAdjList(self):
        for i in range(self.V):
            print("{} : {}".format(i, self.ADJ[i]))

def main():
	g = Graph(6)
	g.addEdge(0, 1)
	g.addEdge(0, 4)
	g.addEdge(2, 1)
	g.addEdge(3, 4)
	g.addEdge(4, 5)
	g.addEdge(2, 3)
	g.addEdge(3, 5)
	g.printAdjList()
	return

if __name__ == '__main__':
	main()
