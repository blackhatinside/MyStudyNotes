class Node:	# graph consists of nodes and its neighbours
	name = ""	# name of the node
	nbrs = []	# neighbours of the node
	def __init__(self, name):
		self.name = name
		self.nbrs = []

from collections import defaultdict as hp	# hashmap[string_key] = node_object

class Graph:	# using adjacency list with Node class
	m = hp(lambda:Node())
	def __init__(self, cities):
		for city in cities:
			self.m[city] = Node(city)

	def addEdge(self, x, y, undir = False):	# directed graph
		self.m[x].nbrs.append(y)
		if undir:
			self.m[y].nbrs.append(x)

	def printAdjList(self):
		for city, node in self.m.items():	# iterate over the hashmap
			print(city, end = "----->")	# key
			for nbr in node.nbrs:
				print(nbr, end = " ")	# values
			print()

def main():
	cities = ["Delhi", "London", "Paris", "New York", ]
	g = Graph(cities)
	g.addEdge("Delhi", "London")
	g.addEdge("New York", "London")
	g.addEdge("Delhi", "Paris")
	g.addEdge("Paris", "New York")
	g.printAdjList()
	return

if __name__ == '__main__':
	main()
