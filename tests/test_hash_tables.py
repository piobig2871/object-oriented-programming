from src.objects.hash_tables import HashTable


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test():
    ht = HashTable(11)
    ht.insert(123, 1)
    ht.insert("test", "value")
    print(ht)
    ht.insert("test", "value2")
    print(ht)
    ht.delete("test")
    print(ht)
    print(ht.T)

print(test())