import node

class linkedList:
    # Constructor
    def __init__(self):
        self.head = None

    # Iterator
    def __iter__(self):
            current = self.head
            while current:
                yield current.val
                current = current.next

    # Adds new node to list
    def add(self, val):
        if self.head is None:
            self.head = node(val)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node(val)

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

    # Prints list
    def printList(self):
        curr = self.head
        while (curr is not None):
            print(curr.val, end=" --> ")
            curr = curr.next
        print('None')

    
