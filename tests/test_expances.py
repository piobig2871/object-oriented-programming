from expanse import MyExpance, summarize_expances


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
