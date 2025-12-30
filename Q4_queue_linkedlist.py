class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        newNode = Node(value)
        if not self.front:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        print("Enqueued:", value)

    def dequeue(self):
        if not self.front:
            print("Underflow")
            return
        value = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        print("Dequeued:", value)

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
