from src.objects.heap_on_three import TriHeapMAX


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test():
    L = [71, 66, 24, 32, 27, 23, 8, 5, 22, 25, 18]
    test = TriHeapMAX(L)
    print(test.sort())

print(test())
