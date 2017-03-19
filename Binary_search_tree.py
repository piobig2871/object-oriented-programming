#Piotr Bigos
#Algorithms and data structures

class binarySearchTree:
    def __init__(self,dane=None):
        self.key = dane
        self.left_node = None
        self.right_node = None

    def bst_insert_nr(self, klucz):
        if self.key is None:
            self.key = klucz
        else:
            z = binarySearchTree(klucz)
            y = None
            x = self
            while (x is not None):
                y = x
                if (z.key < x.key):
                    x = x.left_node
                else:
                    x = x.right_node
            if (z.key < y.key):
                y.left_node = z
            else:
                y.right_node = z

    def inorder(self):
        if self.key is not None:
            if self.left_node is not None:
                self.left_node.inorder()
            print self.key
            if self.right_node is not None:
                self.right_node.inorder()

    def _height(self):
        if self.left_node == None and self.right_node == None:
            return 0
        left = right = 0
        if self.left_node is not None:
            left = self.left_node.height()
        if self.right_node is not None:
            right = self.right_node.height()
        return max(left, right) + 1

    def height(self):
        if self.key == None:
            return -1
        return self._height()

    def _right_is_none(self):
        return self.right_node == None

    def _left_is_none(self):
        return self.left_node == None

    def isleaf(self):
        return self._right_is_none() and self._left_is_none()

    def count_leafs(self):
        if self.isleaf():
            return 1
        left = 0
        if not self._left_is_none():
            left = self.left_node.count_leafs()
        right = 0
        if not self._right_is_none():
            right = self.right_node.count_leafs()
        return left + right

    def _ret_key(self):
        return self.key

    def _search(self, root, key):
        if root  == None:
            return False
        elif root._ret_key() == key:
            return True
        elif root._ret_key() < key:
            return self._search(root.right_node, key)
        else:
            return self._search(root.left_node, key)

    def search(self, x):
        return self._search(self, x)

    def _ret_val(self):
        return self.val

    def _left_is_empty(self):
        if self.left_node == None:
            return True
        else:
            return False

    def _right_is_empty(self):
        if self.right_node == None:
            return True
        else:
            return False

    def isEmpty(self):
        return self.key == None

    def postorder(self):
        if not self._left_is_empty():
            self.left_node.postorder()
        if not self._right_is_empty():
            self.right_node.postorder()
        print self.key

    def preorder(self):
        print self.key
        if not self._left_is_empty():
            self.left_node.preorder()
        if not self._right_is_empty():
            self.right_node.preorder()

    def insert_many(self, *args):
        for i in args:
            self.bst_insert_nr(i)


    def leafsnr(self):
        if self.isEmpty():
            return 0
        if self.isleaf():
            return 1
        ile = 0
        if not self._right_is_none():
            ile += self.right_node.count_leafs()
        if not self._left_is_none():
            ile += self.right_node.count_leafs()
        return ile

    def wierzcholki(self):
        licznik = 1
        if self.left_node:
            licznik += self.left_node.wierzcholki()
        if self.right_node:
            licznik += self.right_node.wierzcholki()
        return licznik

    def depth(self, klucz):
        """ DZIALA """
        if self.isKey(klucz):
            wl = 0
            wr = 0
            if self.key == klucz:
                return wl + wr
            elif klucz < self.key:
                if self.left_node != None:
                    wl = self.left_node.depth(klucz)
            else:
                if self.right_node != None:
                    wr = self.right_node.depth(klucz)
            return wl + wr + 1
        else:
            return -1

    def binary_search_iter(self, val):
        root = self
        while root is not None:
            if val == root.key:
                return True
            elif val < root.key:
                root = root.left_node
            else:
                root = root.right_node
        return False

    def isKey(self, klucz):
        """ DZIALA """
        if self.key is None:
            return False
        if self.key == klucz:
            return True
        elif klucz < self.key:
            if self.left_node != None:
                return self.left_node.isKey(klucz)
            else:
                return False
        else:
            if self.right_node != None:
                return self.right_node.isKey(klucz)
            else:
                return False

    def liscie(self):
        if self == None: return None
        elif self.left_node is None and self.right_node is None:
            print self.key
        else:
            if self.left_node != None: self.left_node.liscie()
            if self.right_node != None: self.right_node.liscie()

    def level2(self):
        if self.key is None:
            return
        if self.left_node and self.right_node:
            print self.key
        if self.left_node:
            self.left_node.level2()
        if self.right_node:
            self.right_node.level2()

    def printLevel(self, lvl):
        if self.key is None: return None
        if lvl == 0:
            print self.key
        if self.left_node is not None: self.left_node.printLevel(lvl-1)
        if self.right_node is not None: self.right_node.printLevel(lvl-1)

    def level2_ktores(self, s):
        if self.key is None:
            return []
        l = []
        if self.left_node and self.right_node:
            l.append(self.key)
        if self.left_node:
            self.left_node.level2()
        if self.right_node:
            self.right_node.level2()






r = binarySearchTree()

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
print r.inorder()
print r.preorder()
print r.postorder()
print r.depth(40)
print r.level2()
print r.level2_ktores(40)
print r.printLevel(3)
print r.binary_search_iter(40)
