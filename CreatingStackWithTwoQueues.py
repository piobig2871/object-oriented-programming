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

        self.kolejka1 = Queue()
        self.kolejka2 = Queue()

    def push(self, val):
        """this method allowes us to push elements in the right order on the stack"""

        self.kolejka2.enqueue(val)
        while not self.kolejka1.isEmpty():
            self.kolejka2.enqueue(self.kolejka1.dequeue())
        while not self.kolejka2.isEmpty():
            self.kolejka1.enqueue(self.kolejka2.dequeue())

    def pop(self):
        """deleting element on the top"""
        return self.kolejka1.dequeue()

    def top(self):
        """top of the stack"""
        return self.kolejka1.first()

    def isEmpty(self):
        """checking if stack is empyt"""
        return self.kolejka1.is_empty()

    def size(self):
        """checking size of the stack"""
        return self.kolejka1.size()
