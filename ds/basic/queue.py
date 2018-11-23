class Queue:
    def __init__(self):
        self.itmes = []

    def isEmpty(self):
        return self.itmes == []

    def enqueue(self, item):
        self.itmes.append(item)

    def dequeue(self):
        item = self.itmes[0]
        self.itmes.remove(item) # self.items.pop(0)
        return item

    def size(self):
        return len(self.itmes)
