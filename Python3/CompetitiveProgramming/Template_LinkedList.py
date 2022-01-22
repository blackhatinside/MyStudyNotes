class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next =  new_node
    def deleteNode(self, position):
        if self.head == None:
            return 
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return 
        for i in range(position -1 ):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return 
        if temp.next is None:
            return 
        next = temp.next.next
        temp.next = None
        temp.next = next 
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next

class Node:
    # __slots__ = ['data', 'next',]
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    # __slots__ = ['head', 'size',]
    def __init__(self):
        self.head = None
        self.size = 0
    def push_front(self, val):      #INSERT AT BEGINNING
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
    def push_back(self, val):       #INSERT AT END
        node = Node(val)
        if self.head == None:
            self.head = node
            #node.next = None BY DEFAULT
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node
            #node.next = None BY DEFAULT
        self.size += 1
    def pop_front(self):        #DELETION AT BEGINNING
        self.head = self.head.next
        self.size -= 1
    def pop_back(self):         #DELETION AT ENDING
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None # OR temp.next.next
        self.size -= 1
    def rotate_list(self, n):       #CLOCKWISE ROTATION
        if n == 0:
            return
        n = n % self.size
        temp = self.head
        cnt = 1
        while cnt < n:
            temp = temp.next
            cnt = cnt + 1
        beg = temp
        while temp.next != None:
            temp = temp.next
        temp.next = self.head
        self.head = beg.next
        beg.next = None
    def reverse_list(self):     #REVERSAL USING ITERATIVE APPROACH
        prv = nxt = None
        cur = self.head
        while cur != None:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        self.head = prv
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
