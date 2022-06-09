class Node:     # complex node (graph edge) class
    NAME = ""
    NEIGHBOURS = []

    def __init__(self, name):
        self.NAME = name
        self.NEIGHBOURS = []

class Graph:    # complex graph using adjacency lists
    HP = dict() # hashmap[key] = node object
    def __init__(self, cities):
        for city in cities:
            self.HP[city] = Node(city)

    def addEdge(self, x, y, undir = False):     # directed graph
        self.HP[x].NEIGHBOURS.append(y)
        if undir:
            self.HP[y].NEIGHBOURS.append(x)

    def printAdjList(self):
        for city, node in self.HP.items():
            print(city, end = "----->")
            print("{} : {}".format(node.NAME, node.NEIGHBOURS))

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
