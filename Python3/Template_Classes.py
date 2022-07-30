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

class MaxHeapObj(object):
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        return self.val > other.val
    def __eq__(self, other):
        return self.val == other.val
    def __str__(self):
        return str(self.val)

class MinHeap(object):
    def __init__(self):
        self.h = []
    # insertion - push()
    def heappush(self, x):
        heapq.heappush(self.h, x)
    # deletion - pop()
    def heappop(self):
        return heapq.heappop(self.h)
    # fetch - hq[i]
    def __getitem__(self, i):
        return self.h[i]
    # len(hq)
    def __len__(self):
        return len(self.h)
    def heapify(self, arr):
        for val in arr:
            heapq.heappush(self.h, MaxHeapObj(val))

class MaxHeap(MinHeap):
    def heappush(self, x):
        heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self):
        return heapq.heappop(self.h).val
    def __getitem__(self, i):
        return self.h[i].val
    def heapify(self, arr):
        for val in arr:
            heapq.heappush(self.h, MaxHeapObj(val))
