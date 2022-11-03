from src.objects.stack import Stack

# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test():
    s = Stack()
    s.insert_many([0, 1, 2, 3, 4, 5])
    print(s.pop())
    print(s.pop())


print(test())
