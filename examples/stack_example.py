from data_structures.stack import Stack

def test_stack():
    Q = Stack()
    Q.print_stack()
    Q.push(1)
    Q.push(2)
    Q.push(3)
    print(f'Next in stack is: {Q.peek()}')
    Q.print_stack()
    print(f'Come here {Q.pop()}, Let me serve you ;)')
    Q.print_stack()
    Q.empty()
    Q.print_stack()

if __name__ == "__main__":
    test_stack()