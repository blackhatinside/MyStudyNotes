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

	def DFS(self, source):
		arr = []
		visited = [0] * self.V
		def helperDFS(node):
			visited[node] = 1
			arr.append(node)
			for ele in self.l[node]:
				if not visited[ele]:
					helperDFS(ele)
		helperDFS(source)
		return arr

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
