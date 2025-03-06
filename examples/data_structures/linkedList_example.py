from data_structures.linkedList import LinkedList

def test_linked_list():
    ll = LinkedList()
    print("Created an empty linked list.")
    ll.printList()

    ll.add(1)
    ll.add(2)
    ll.add(3)
    print("\nAfter adding nodes:")
    ll.printList()

    print("\nTesting iteration:")
    for val in ll:
        print(val, end=" ")


    assert ll.is_node(1) == True
    assert ll.is_node(2) == True
    assert ll.is_node(3) == True
    assert ll.is_node(4) == False
    print("is_node() test passed")

    ll.remove(2)
    ll.printList()
    assert ll.is_node(2) == False
    print("Node removal test passed")

    ll.remove(1)
    ll.printList()
    assert ll.is_node(1) == False
    print("Head removal test passed")

    ll.remove(3)
    ll.printList()
    assert ll.is_node(3) == False
    print("Last node removal test passed")

    assert ll.head is None
    print("List is empty")

if __name__ == "__main__":
    test_linked_list()