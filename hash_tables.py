class HashTable(object):
    """Hash Table using open addressing"""

    def __init__(self, size):
        self.size = size
        self.T = []
        for i in range(self.size):
            self.T.append(None)

    def hprim(self, key):
        """Hash function using modulo operation."""
        return key % self.size

    def hstring(self, key):
        """String hash function using modulo."""
        temp = 0
        for i in key:
            temp += ord(i)
        return temp % self.size

    def _gen_sequence(self, key):
        """generate key sequence for inteegers and floats."""
        seq = []
        for idx in range(self.size):
            seq.append((self.hprim(key) + idx) % self.size)
        return seq

    def _gen_sequence_str(self, key):
        """generate key sequence for strings."""
        seq = []
        for idx in range(self.size):
            seq.append((self.hstring(key) + idx) % self.size)
        return seq

    def _slot_is_empty(self, idx):
        """Check if slot is empty."""
        return self.T[idx] is None or self.T[idx] == 'Deleted'

    def insert_int(self, key, val):
        """Add value into hash table."""
        seq = self._gen_sequence(key)
        flag, idx = self._search(key)
        if not flag:
            for idx in seq:
                if self._slot_is_empty(idx):
                    self.T[idx] = (key, val)
                    break
            else:
                raise IndexError("Hash table is full!")
        else:
            self.T[idx] = key, val

    def insert_str(self, key, val):
        """Add string value into hashtable."""
        seq = self._gen_sequence_str(key)
        flag, idx = self._search(key)
        if not flag:
            for idx in seq:
                if self._slot_is_empty(idx):
                    self.T[idx] = (key, val)
                    return None
            raise IndexError("Hash table is full!")
        self.T[idx] = key, val

    def insert(self, key, val):
        """Add key and value into hash table."""
        if type(key) == str:
            return self.insert_str(key, val)
        else:
            return self.insert_int(key, val)

    def _search(self, key):
        """Search in hash table."""
        if type(key) == int:
            seq = self._gen_sequence(key)
        else:
            seq = self._gen_sequence_str(key)
        for idx in seq:
            if self.T[idx] is None:
                return False, -1
            elif self.T[idx][0] == key:
                return True, idx
        return False, -1

    def delete(self, key):
        """Deletion element from """
        flag, idx = self._search(key)
        if flag:
            self.T[idx] = 'Deleted'
        else:
            raise Exception("There is not such a key")

    def get_val(self, key):
        """Getting value from hash table"""
        ret, idx = self._search(key)
        if ret:
            return self.T[idx][1]
        else:
            raise KeyError("There is not such a key")

    def __str__(self):
        """reprezentation"""
        ret = "{"
        for val in self.T:
            print(val)
            if val is not None and val != 'Deleted':
                ret += str(val[0]) + ': ' + str(val[1]) + ', '
        return ret[:-2] + '}'


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
