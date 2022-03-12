# arr = [6, 1, 3, 4, 2, 7, 5, 8, 10, 9, 0]

def selectionSort(arr, n):  #arr is the array and n is the size of the array
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubbleSort(arr, n):  #arr is the array and n is the size of the array
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertionSort(arr, n):  #arr is the array and n is the size of the array
    for i in range(1, n):
        cur = arr[i]
        j = i - 1
        while arr[j] > cur and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = cur
    return arr

class Queue:    #queue implementation using Python list to help in BFS
	queue = []
	def __init__(self):
		self.queue = []
	def enqueue(self, x):
		self.queue.append(x)
	def dequeue(self):
		return self.queue.pop(0)
	def __len__(self):
		return len(self.queue)
class Graph:	# graph implementation using adjacency lists
	V = 0	# number of vertices
	l = [[], ]	# adjacency list
	def __init__(self, v = 0):	# constructor
		self.V = v
		self.l = [list() for _ in range(self.V)]
	def addEdge(self, i, j, undir = True):
		self.l[i].append(j)
		if undir:	# undirected graph has both A -> B and B -> A connections
			self.l[j].append(i)
	def BFS(self, graph, source):
		visited = collections.defaultdict(lambda:False)
		ans = list()
		q = Queue()
		q.enqueue(source)
		visited[source] = True
		while len(q) > 0:
			ele = q.dequeue()
			ans.append(ele)
			for x in self.l[ele]:
				if not visited[x]:
					q.enqueue(x)
					visited[x] = True
		return ans
	def printAdjList(self):
		for ii in range(len(self.l)):
			x = self.l[ii]
			print(ii, *x)
