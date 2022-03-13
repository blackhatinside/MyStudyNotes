# Shortest Path from Source to all other vertices
# Shortest Distance from Source to all other vertices
from collections import defaultdict

class Queue:
	queue = []
	def __init__(self):
		self.queue = []
	def enqueue(self, nbr):
		self.queue.append(nbr)
	def dequeue(self):
		return self.queue.pop(0)
	def __len__(self):
		return len(self.queue)

class Graph:	# using adjacency lists
	V = 0	# number of vertices
	l = [[], ]	# adjacency list
	def __init__(self, v = 0):	# constructor
		self.V = v	# len(self.l)
		self.l = [list() for _ in range(self.V)]

	def addEdge(self, i, j, undir = True):
		self.l[i].append(j)
		if undir:	# undirected graph has both A -> B and B -> A connections
			self.l[j].append(i)

	def BFS(self, graph, source, destination = -1):	# O(vertices + edges)
		visited = [0] * self.V
		parent = [-1] * self.V 
		dist = [0] * self.V
		dist[source] = 0
		parent[source] = source
		ans = list()
		q = Queue()
		q.enqueue(source)
		visited[source] = 1
		while len(q) > 0:
			ele = q.dequeue()
			ans.append(ele)
			for nbr in self.l[ele]:
				if not visited[nbr]:
					q.enqueue(nbr)
					parent[nbr] = ele
					dist[nbr] = dist[ele] + 1 
					visited[nbr] = 1
		def printShortestPathToAllNodes():
			for i in range(self.V):
				print("Shortest Distance from {} to {} is {}".format(source, i, dist[i]))
		printShortestPathToAllNodes()
		def printPathFromSourceToDestination():
			path = []
			if destination != -1:
				temp = destination
				while temp != source:
					path.append(temp)
					temp = parent[temp]
			path.append(source)
			return path
		print("Path from Source to Destination:", *printPathFromSourceToDestination())
		return ans

	def printAdjList(self):
		for ii in range(self.V):
			nbr = self.l[ii]
			print(ii, *nbr)

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
	return

if __name__ == '__main__':
	main()
