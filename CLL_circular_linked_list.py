class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    def display(self):
        if self.head is None:
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()
