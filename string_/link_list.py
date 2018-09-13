class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        return

class LinkList:
    def __init__(self):
        self.head = ListNode()

    def add_item(self, data):
        new_node = ListNode(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def get_length(self):
        length = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            length = length + 1
        return length

    def display(self):
        eles = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            val = cur_node.data
            eles.append(val)
        return eles

    def find_item(self, idx):
        if idx >= self.get_length():
            print('Error: Get Index out of range!')
            return
        cur_idx = 0
        cur_node = self.head
        while True:
#            print('here')
            cur_node = cur_node.next
            if cur_idx == idx:
                return print('element at {} index: {}'.format(idx, cur_node.data))
            cur_idx = cur_idx + 1

    def del_item(self, idx):
        if idx >= self.get_length():
            print('Error: Get Index out of range!')
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            pre_node = cur_node
            cur_node = cur_node.next
            if idx == cur_idx:
                pre_node.next = cur_node.next
                return print('linked list after deleting: {}'.format(self.display()))
            cur_idx = cur_idx + 1

#l = LinkList()
#l.add_item(1)
#l.add_item(2)
#l.add_item(3)
#l.add_item(4)
#print(l.display())
#l.find_item(2)
#l.del_item(2)
##l.display()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
