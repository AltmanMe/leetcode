from link_node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        cur = self.head
        pre = None
        stop = False
        while cur and not stop:
            if cur.get_data() > item:
                stop = True
            else:
                pre = cur
                cur = cur.get_next()

        node = Node(item)
        if pre: # pre is not head node
            pre.set_next(node)
            node.set_next(cur)
        else: # pre is head node
            self.head = node
            node.set_next(cur)

    def size(self):
        cur = self.head
        cnt = 0
        while cur:
            cnt = cnt + 1
            cur = cur.get_next()
        return cnt

    def search(self,item):
        cur = self.head
        found = False
        stop = False
        while cur and not stop:
            if cur.get_data() == item:
                found = True
                break
            else:
                if cur.get_data() > item: # cause we do not need to continue searching after current value is bigger than target
                    stop = True
                else:
                    cur = cur.get_next()
        return found

    def remove(self,item):
        cur = self.head
        pre = None
        while cur:
            if cur.get_data() == item:
                if pre: # previous node is not head
                    pre.set_next(cur.get_next())
                else: # previous node is head
                    self.head = cur.get_next()
                break
            else:
                pre = cur
                cur = cur.get_next()
        
if __name__ == '__main__':

    mylist = OrderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))
