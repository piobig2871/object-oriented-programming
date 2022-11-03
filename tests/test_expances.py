from src.objects.expanse import MyExpance, summarize_expances


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test():
    foo = []
    foo.append(MyExpance('food', 4))
    foo.append(MyExpance('food', 3))
    foo.append(MyExpance('car', 3))
    foo.append(MyExpance('dog', 1))
    summarize_expances(2, foo)
    print(foo)
    return True


print(test())
