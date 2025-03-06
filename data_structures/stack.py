from linkedList import LinkedList
from node import Node

class Stack():
    def __init__(self):
        self.list = LinkedList()
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def push(self, val):
        node = self.list.head
        self.list.head = Node(val)
        self.list.head.next = node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None

        head = self.list.head.val
        self.list.head = self.list.head.next
        self.size -= 1
        return head
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list.head.val
    
    def empty(self):
        self.list.head = None
        self.size = 0
    
    def print_stack(self):
        print('Stack top: ', end='')
        self.list.printList()
