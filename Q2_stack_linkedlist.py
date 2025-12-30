class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        print("Pushed:", value)

    def pop(self):
        if self.isEmpty():
            print("Underflow")
            return
        value = self.top.data
        self.top = self.top.next
        print("Popped:", value)

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        print("Top element:", self.top.data)

    def printStack(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
