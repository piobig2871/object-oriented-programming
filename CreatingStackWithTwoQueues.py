class Queue:

    '''Class Queue we will be using instances of this class to create stack.
        Queue is data stucture FIFO type.'''

    def __init__(self):
        self.tab = []

    def isEmpty(self):

        return len(self.tab) == 0

    def enqueue(self, item):

        return self.tab.insert(0, item)

    def dequeue(self):

        if self.isEmpty(): raise IndexError('You can`t delete item from empty list ')
        return self.tab.pop()

    def size(self):

        return len(self.tab)

    def printqueue(self):

        print self.tab

    def first(self):

        if self.isEmpty(): raise IndexError('The list is empty')
        return self.tab[-1]


class CreatingStackWithTwoQueues:

    def __init__(self):

        self.kolejka1 = Queue() #First instance of Queue class
        self.kolejka2 = Queue() #Second instance of Queue class

    def push(self, val):

        '''this method allowes us to push elements in the right order on the stack'''

        self.kolejka2.enqueue(item)
        while not self.kolejka1.isEmpty():
            self.kolejka2.enqueue(self.kolejka1.dequeue())
        while not self.kolejka2.isEmpty():
            self.kolejka1.enqueue(self.kolejka2.dequeue())

    def pop(self):

        '''deleting element on the top'''

        return self.kolejka1.dequeue()

    def top(self):

        '''top of the stack'''

        return self.kolejka1.first()

    def isEmpty(self):

        '''checking if stack is empyt'''

        return self.kolejka1.isEmpty()

    def size(self):

        '''checking size of the stack'''

        return self.kolejka1.size()
