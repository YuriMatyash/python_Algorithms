from data_structures.queue import Queue

def test_queue():
    Q = Queue()
    Q.print_queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print(f'Next in queue is: {Q.peek()}')
    Q.print_queue()
    print(f'Come here {Q.dequeue()}, Let me serve you ;)')
    Q.print_queue()
    Q.empty()
    Q.print_queue()

if __name__ == "__main__":
    test_queue()