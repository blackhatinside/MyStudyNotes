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
