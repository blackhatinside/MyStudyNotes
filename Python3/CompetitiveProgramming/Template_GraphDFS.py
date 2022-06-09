class Graph:	# using adjacency lists
	V = 0	# number of vertices
	l = [[], ]	# adjacency list
	def __init__(self, v = 0):	# constructor
		self.V = v
		self.l = [list() for _ in range(self.V)]

	def addEdge(self, i, j, undir = True):
		self.l[i].append(j)
		if undir:	# undirected graph has both A -> B and B -> A connections
			self.l[j].append(i)

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
	print(g.DFS(0))
	return

if __name__ == '__main__':
	main()
