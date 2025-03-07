from data_structures.linkedList import LinkedList

class Queue():
    def __init__(self):
        self.list = LinkedList()
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def enqueue(self, val):
        self.list.add(val)
        self.size += 1
    
    def dequeue(self):
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
        while self.list.head != None:
            self.dequeue()

    def print_queue(self):
        print('Queue front: ',end='')
        self.list.printList()