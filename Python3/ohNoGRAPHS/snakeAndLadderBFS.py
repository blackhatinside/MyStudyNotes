# CALL YOUR MODULES HERE	-------------------->
# import bisect, heapq
# import fractions, math, numpy
# import atexit, io, os, sys, time
#		<----------------------------------------

# DEFINE YOUR FASTIO HERE	-------------------->
# # 0 in os.read() indicated file descriptor for standard input (STDIN)
# # os.fstat(0).st_size will tell Python how many bytes are currently waiting in the STDIN buffer
# # Then os.read() will read those bytes in bulk from STDIN, producing a bytestring
# inputt = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# # A lambda function to get integer input and return it
# input = lambda: inputt()   # integers
# # A lambda function to get string input and return it
# # input = lambda: inputt().decode().strip()   # strings
# # ss = sys.stdout
# ss = io.BytesIO()
# _write = ss.write
# ss.write = lambda s: _write(s.encode())
# atexit.register(lambda: os.write(1, ss.getvalue()))
#		<----------------------------------------

# DEFINE YOUR FUNCTIONS HERE	-------------------->
# def readnumbers(zero=0):
#     _ord, nums, num, neg = lambda nbr: nbr, [], zero, False
#     i, s = 0, io.BytesIO(os.read(0,os.fstat(0).st_size)).read()
#     try:
#         while True:
#             if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
#             elif s[i] == b"-"[0]:neg = True
#             elif s[i] != b"\r"[0]:
#                 nums.append(-num if neg else num)
#                 num, neg = zero, False
#             i += 1
#     except IndexError:
#         pass
#     if s and s[-1] >= b"0"[0]: nums.append(-num if neg else num)
#     return nums
# def FastInt(zero=0):
#     _ord, nums, num, neg = lambda nbr: nbr, [], zero, False
#     i, s = 0, io.BytesIO(os.read(0,os.fstat(0).st_size)).read()
#     try:
#         while True:
#             if s[i] >= b"0"[0]:num = 10 * num + _ord(s[i]) - 48
#             elif s[i] == b"-"[0]:neg = True
#             elif s[i] != b"\r"[0]:
#                 nums.append(-num if neg else num)
#                 num, neg = zero, False
#             i += 1
#     except IndexError:
#         pass
#     if s and s[-1] >= b"0"[0]: nums.append(-num if neg else num)
#     return nums
#		<----------------------------------------

# ENTER YOUR CODE HERE	-------------------->

# User function Template for Python3

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

class Graph:    # using adjacency lists
    V = 0    # number of vertices
    l = [[], ]    # adjacency list
    def __init__(self, v = 0):    # constructor
        self.V = v    # len(self.l)
        self.l = [list() for _ in range(self.V)]

    def addEdge(self, i, j, undir = False):
        self.l[i].append(j)
        if undir:    # undirected graph has both A -> B and B -> A connections
            self.l[j].append(i)

    def BFS(self, source, destination = -1):    # O(vertices + edges)
        visited = [0] * self.V
        dist = [0] * self.V
        parent = [-1] * self.V
        q = Queue()
        q.enqueue(source)
        dist[source] = 0
        visited[source] = 1
        parent[source] = source
        while len(q) > 0:
            ele = q.dequeue()
            for nbr in self.l[ele]:
                if not visited[nbr]:
                    q.enqueue(nbr)
                    dist[nbr] = dist[ele] + 1 
                    parent[nbr] = ele
                    visited[nbr] = 1
        def printShortestPathToAllNodes():
            for i in range(self.V):
                print("Shortest Distance from {} to {} is {}".format(source, i, dist[i]))
        # printShortestPathToAllNodes()
        def printPathFromSourceToDestination():
            path = []
            if destination != -1:
                temp = destination
                while temp != source:
                    path.append(temp)
                    temp = parent[temp]
            path.append(source)
            return path[::-1]
        print("Path from Source to Destination:", *printPathFromSourceToDestination())
        return dist[destination]

import collections
class Solution:
    def minThrow(self, N, arr):
        # code here
        n = 31
        board = collections.defaultdict(lambda:0)
        for i in range(0, 2 * N, 2):
            board[arr[i]] = arr[i + 1] - arr[i]
        g = Graph(n)
        for u in range(1, n):
            for dice in range(1, 7):
                v = u + dice
                v += board[v]
                if v < n:
                    g.addEdge(u, v) # move within the board
        return g.BFS(1, 30)
            

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends


#		<----------------------------------------

# ENTER YOUR NOTES HERE	-------------------->
'''		# NOTES	- uncomment line to run this block

Python Competitive Programming Template for FAST I/O 

# '''
#		<----------------------------------------
