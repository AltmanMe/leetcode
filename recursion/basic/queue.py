import time
from stack import Stack

class Queue:
    def __init__(self):
        self.itmes = []

    def isEmpty(self):
        return self.itmes == []

    def enqueue(self,item):
        self.itmes.append(item)

    def dequeue(self):
        item = self.itmes[0]
        self.itmes.remove(item) # self.items.pop(0)
        return item

    def size(self):
        return len(self.itmes)

    def traverse(self):
        print(self.itmes)

class Queue2:
    def __init__(self):
        self.itmes = []

    def isEmpty(self):
        return self.itmes == []

    def enqueue(self,item):
        self.itmes.insert(0,item)

    def dequeue(self):
        return self.itmes.pop()

    def size(self):
        return len(self.itmes)

    def traverse(self):
        print(self.itmes)

class Queue3:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def isEmpty(self):
        return self.inbox.isEmpty() and self.outbox.isEmpty()

    def enqueue(self,item):
        self.inbox.push(item)
    
    def dequeue(self):
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                value = self.inbox.pop()
                self.outbox.push(value)
        else:
            return self.outbox.pop()

    def size(self):
        return self.inbox.size() + self.outbox.size

if __name__ == '__main__':
    """
    Benchmark comparisons of the two queue implementations
    """

    que1 = Queue()
    que2 = Queue2()
    que3 = Queue3()
    que_list = [que1, que2, que3]

    for i in range(3):
        start = time.time()
        que = que_list[i]
        for j in range(int(1e5)): # less than 1e5
            que.enqueue(j)
        print('Enqueue Time Usage: {}'.format(time.time()-start))

    for i in range(3):
        start = time.time()
        que = que_list[i]
        for j in range(int(1e5)):
            que.dequeue()
        print('Dequeue Time Usage: {}'.format(time.time()-start))
