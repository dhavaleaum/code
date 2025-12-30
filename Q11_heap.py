class MaxHeap:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)
        self.data.sort(reverse=True)

    def delete(self):
        return self.data.pop(0)

class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, val):
        self.data.append(val)
        self.data.sort()

    def delete(self):
        return self.data.pop(0)
