class Queue:
    """Class Queue we will be using instances of this class to create stack.
        Queue is data stucture FIFO type."""

    def __init__(self):
        self.tab = []

    def is_empty(self):
        return len(self.tab) == 0

    def enqueue(self, item):
        return self.tab.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('You can`t delete item from empty list ')
        return self.tab.pop()

    def size(self):
        return len(self.tab)

    def __repr__(self):
        print(self.tab)

    def first(self):
        if self.is_empty():
            raise IndexError('The list is empty')
        return self.tab[-1]


class CreatingStackWithTwoQueues:

    def __init__(self):

        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, val):
        """this method allowes us to push elements in the right order on the stack"""

        self.queue2.enqueue(val)
        while not self.queue1.is_empty():
            self.queue2.enqueue(self.queue1.dequeue())
        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

    def pop(self):
        """deleting element on the top"""
        return self.queue1.dequeue()

    def top(self):
        """top of the stack"""
        return self.queue1.first()

    def is_empty(self):
        """checking if stack is empyt"""
        return self.queue1.is_empty()

    def size(self):
        """checking size of the stack"""
        return self.queue1.size()
