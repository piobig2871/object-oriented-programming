class Stack:
    def __init__(self):
        self.tab = list()

    def is_empty(self):
        return len(self.tab) == 0

    def top(self):
        if self.is_empty:
            raise KeyError("Empty stack")
        else:
            return self.tab[-1]

    def push(self, item):
        self.tab.append(item)

    def insert_many(self, *args):
        for val in list(*args):
            self.push(val)

    def pop(self):
        if self.is_empty():
            raise KeyError('Empty stack')
        else:
            temp = self.tab[-1]
            del (self.tab[-1])
            return temp

    def size(self):
        return len(self.tab)


s = Stack()
s.insert_many([0, 1, 2, 3, 4, 5])
print(s.pop())
print(s.pop())
