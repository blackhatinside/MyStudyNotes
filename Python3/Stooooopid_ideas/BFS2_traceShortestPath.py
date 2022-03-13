from collections import defaultdict

class Queue:
	queue = []
	def __init__(self):
		self.queue = []
	def enqueue(self, x):
		self.queue.append(x)
	def dequeue(self):
		return self.queue.pop(0)
	def __len__(self):
		return len(self.queue)

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

	def BFS(self, graph, source, destination):
		visited = defaultdict(lambda:False)
		ans = []
		q = Queue()
		q.enqueue([source])
		visited[source] = True
		while q:
			path = q.dequeue()
			node = path[-1]
			if node == destination:
				return path
			if node > len(self.l):
				adjacents = []
			else:
				adjacents = self.l[node]
			for x in adjacents:
				new_path = list(path)
				new_path.append(x)
				q.enqueue(new_path)
		return []

	def printAdjList(self):
		for ii in range(self.V):
			x = self.l[ii]
			print(ii, *x)

def main():
	g = Graph(7)
	g.addEdge(1, 2)
	g.addEdge(1, 0)
	g.addEdge(2, 3)
	g.addEdge(0, 4)
	g.addEdge(3, 5)
	g.addEdge(4, 5)
	g.addEdge(5, 6)
	print(*g.BFS(g, 1, 6))
	# g.printAdjList()
	return

if __name__ == '__main__':
	main()
