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
    else:
        stack.append([x, 1])
