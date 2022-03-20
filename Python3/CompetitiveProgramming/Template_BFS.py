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

class Graph:    # using adjacency lists
    V = 0   # number of vertices
    l = [[], ]  # adjacency list
    def __init__(self, v = 0):  # constructor
        self.V = v  # len(self.l)
        self.l = [list() for _ in range(self.V)]

    def addEdge(self, i, j, undir = True):
        self.l[i].append(j)
        if undir:   # undirected graph has both A -> B and B -> A connections
            self.l[j].append(i)

    def BFS(self, graph, source):   # O(vertices + edges)
        visited = defaultdict(lambda:False)
        # visited = set()
        ans = list()
        q = Queue()
        q.enqueue(source)
        visited[source] = True
        # visited.add(source)
        while len(q) > 0:
            ele = q.dequeue()
            ans.append(ele)
            for x in self.l[ele]:
                if not visited[x]:
                # if x not in visited:
                    q.enqueue(x)
                    visited[x] = True
                    # visited.add(x)
        return ans

    def printAdjList(self):
        for ii in range(self.V):
            x = self.l[ii]
            print(ii, *x)

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
	print(*g.BFS(g, 1))
	return

if __name__ == '__main__':
	main()
