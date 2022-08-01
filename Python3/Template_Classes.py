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

class Multiset:
    def __init__(self):
        self.items = []
    def add(self, val):
        #adds o occurrence of val from the multiset, if any
        return self.items.append(val)
        pass
    def remove(self, val):
        # removes o occurrence of val from the multiset, if any
        if self.items.count(val) != 0:
            return self.items.remove(val)
        pass
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.items
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.items)

    class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])
    def __delitem__(self, idx):
        self[idx] = self._default
    def __getitem__(self, idx):
        return self.data[idx + self._size]
    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1
    def __len__(self):
        return self._len
    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size
        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1
        return self._func(res_left, res_right)
    def __repr__(self):
        return "SegmentTree({0})".format(self.data)
    
class SegmentTree:
    def __init__(self, array, func=max):
        self.n = len(array)
        self.size = 2**(int(log2(self.n-1))+1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != min else inf
        self.data = [self.default] * (2 * self.size)
        self.process(array)
    def process(self, array):
        self.data[self.size : self.size+self.n] = array
        for i in range(self.size-1, -1, -1):
            self.data[i] = self.func(self.data[2*i], self.data[2*i+1])
    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        res = self.default
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                alpha += 1
            if omega & 1:
                omega -= 1
                res = self.func(res, self.data[omega])
            alpha >>= 1
            omega >>= 1
        return res
    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2*index], self.data[2*index+1])
            index >>= 1
