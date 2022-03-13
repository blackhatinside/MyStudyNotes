# create a square matrix
def squareMatrix(n):
    grid = [[0] * n for _ in range(n)]
    return grid


# create a 2D matrix
def Matrix2D(rows, cols):
    grid = [[0 for j in range(cols)] for i in range(rows)]
    return grid


class LinkedListNode:
    # __slots__ = ['data', 'next',]
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


# sort a 2D array named "grid"
grid.sort(key = lambda x: (x[0], x[1]))

# squeeze consecutive repeating elements in an array by replacing them with a single element (stack implementation)
stack = []
for x in arr:
    if not stack:
        stack.append([x, 1])
    elif stack[-1][0] == x:
        stack[-1][1] += 1
        
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


# inorder traversal : left child -->> root -->> right child
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else list()

# queue implementation using Python list to help in BFS
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
    
# graph implementation using adjacency lists
class Graph:
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
    else:
        stack.append([x, 1])
