from data_structures.node import Node, Color

def test_node():
    node1 = Node(1)
    print(f'Created new Node with val of:{node1.val}, and color of:{node1.color}')
    node2 = Node(2)
    print(f'Created new Node with val of:{node2.val}, and color of:{node1.color}')
    node1.next = node2
    print(f'Node1 is connected to:{node1.next}')
    print(f'Node2 is connected to:{node2.next}')
    print(f'node2 through node1.... {node1.next.val}')

    node1.toGray()
    print(f'it is: {node1.isGray()}, that node1 is Gray')

    node1.toBlack()
    print(f'it is: {node1.isBlack()}, that node1 is Black')
    print(f'what about white? {node1.isWhite()}')

if __name__ == "__main__":
    test_node()