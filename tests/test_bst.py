from src.objects.binary_search_tree import BinarySearchTree


# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


def test_binary_search_tree():
    r = BinarySearchTree()
    r.bst_insert_nr(65)
    r.bst_insert_nr(54)
    r.bst_insert_nr(59)
    r.bst_insert_nr(51)
    r.bst_insert_nr(48)
    r.bst_insert_nr(41)
    r.bst_insert_nr(36)
    r.bst_insert_nr(53)
    r.bst_insert_nr(57)
    r.bst_insert_nr(63)
    r.bst_insert_nr(40)
    r.bst_insert_nr(52)
    r.bst_insert_nr(58)
    print(f'Inorder: {r.inorder()}')
    print(f'Preorder:{r.preorder()}')
    print(f'Postorder: {r.postorder()}')
    print(f'Leafs of the tree: {r.leafs()}')
    print(f'Depth of the value 40: {r.depth(40)}')
    print(f'Second level of the tree: {r.level2()}')
    print(f'Third level of the tree: {r.print_level(3)}')
    print(f'Find value 40: {r.binary_search_iter(40)}')
