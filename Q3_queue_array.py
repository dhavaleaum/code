MAX = 100

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = -1
        self.count = 0
        self.data = [None] * MAX

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == MAX

    def enqueue(self, value):
        if self.isFull():
            print("Overflow")
            return
        self.rear = (self.rear + 1) % MAX
        self.data[self.rear] = value
        self.count += 1
        print("Enqueued:", value)

    def dequeue(self):
        if self.isEmpty():
            print("Underflow")
            return
        value = self.data[self.front]
        self.front = (self.front + 1) % MAX
        self.count -= 1
        print("Dequeued:", value)

    def printQueue(self):
        idx = self.front
        for _ in range(self.count):
            print(self.data[idx], end=" ")
            idx = (idx + 1) % MAX
        print()
