MAX = 100

class Stack:
    def __init__(self):
        self.maxSize = MAX
        self.top = -1
        self.data = [None] * self.maxSize

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.maxSize - 1

    def push(self, value):
        if self.isFull():
            print("Overflow")
            return
        self.top += 1
        self.data[self.top] = value
        print("Pushed:", value)

    def pop(self):
        if self.isEmpty():
            print("Underflow")
            return
        value = self.data[self.top]
        self.top -= 1
        print("Popped:", value)

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        print("Top element:", self.data[self.top])

    def printStack(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        for i in range(self.top + 1):
            print(self.data[i], end=" ")
        print()
