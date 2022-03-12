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

	def printAdjList(self):
		for ii in range(len(self.l)):
			x = self.l[ii]
			print(ii, *x)

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
