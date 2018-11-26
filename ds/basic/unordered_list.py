from link_node import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node
        self.length = self.length + 1

    def size(self):
#        cur = self.head
#        cnt = 0
#        while cur:
#            cnt = cnt + 1
#            cur = cur.get_next()
#        return cnt
        return self.length

    def search(self,item):
        cur = self.head
        found = False
        while cur:
            if cur.get_data() == item:
                found = True
                break
            else:
                cur = cur.get_next()
        return found

    def remove(self,item):
        cur = self.head
        pre = None
        while cur:
            if cur.get_data() == item:
                if pre: # previous node is not head node
                    pre.set_next(cur.get_next())
                else: # previous node is head node
                    self.head = cur.get_next()
                break
            else:
                pre = cur
                cur = cur.get_next()
        self.length = self.length - 1

    def append(self,item):
        cur = self.head
        pre = None
        node = Node(item)
        if cur: # Current list is not empty
            while cur:
                pre = cur
                cur = cur.get_next()
            pre.set_next(node)
        else:
            self.head = node
        self.length = self.length + 1

    def index(self,item):
        cur = self.head
        idx = 0
        while cur:
            if cur.get_data() == item:
                return idx
            cur = cur.get_next()
            idx = idx + 1
        return None

    def __str__(self):
        result = "["
        node = self.head
        if node != None:
            result += str(node.data)
            node = node.next
            while node:
                result += ", " + str(node.data)
                node = node.next
        result += "]"
        return result 
        
if __name__ == '__main__':

    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print(mylist)
    print(mylist.size())
    print(mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print(mylist.search(93))
