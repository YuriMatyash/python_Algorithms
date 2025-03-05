from node import Node

class LinkedList:
    # Constructor
    def __init__(self, val=None):
        if val is None:
            self.head = None
        else:
            self.head = Node(val)

    # Iterator
    def __iter__(self):
            current = self.head
            while current:
                yield current.val
                current = current.next

    # Adds new node to list
    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)

    # Removes node from list
    def remove(self, val):
        if self.head is None:
            return
        
        if self.head.val == val:
            self.head = self.head.next
            return
        
        curr = self.head
        prev = None
        while curr is not None and curr.val != val:
            prev = curr
            curr = curr.next 
        if curr is not None:
            prev.next = curr.next

    # Returns True if node exsists, else false
    def is_node(self, val):
        if self.head == None:
            return False
        
        curr = self.head
        while (curr is not None):
            if curr.val == val:
                return True
            curr = curr.next
        
        return False


    # Prints list
    def printList(self):
        curr = self.head
        while (curr is not None):
            print(curr.val, end=" --> ")
            curr = curr.next
        print('None')

    
