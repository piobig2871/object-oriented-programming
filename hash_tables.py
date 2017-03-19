class HashTable(object):
    """Klasa realizujaca tablice mieszajace
       z adresowaniem otwartym"""

    def __init__(self, size):
        self.size = size
        self.T = []
        for i in xrange(self.size):
            self.T.append(None)
    
    def hprim(self, key):
        """zwykla funkcja haszujaca"""
        return key % self.size
    
    def hstring(self, key):
        """zwykla funkcja haszujaca string"""
        temp = 0
        for i in key:
            temp += ord(i)
        return temp % self.size
           
    def _gen_sequence(self, key):
        """funkcja generujaca sekwencje kluczy"""
        seq = []
        for idx in xrange(self.size):
            seq.append((self.hprim(key) + idx) % self.size)
        return seq
    
    def _gen_sequence_str(self, key):
        seq = []
        for idx in xrange(self.size):
            seq.append((self.hstring(key) + idx) % self.size)
        return seq

    def _slot_is_empty(self, idx):
        return self.T[idx] == None or self.T[idx] == 'Deleted'
   
    def insert_int(self, key, val):
        """funkcja wstawiajaca klucz int do tablicy"""
        seq = self._gen_sequence(key)
        flag, idx = self._search(key)
        if not flag:
            for idx in seq:
                if self._slot_is_empty(idx):
                    self.T[idx] = (key, val)
                    break
            else:
                raise IndexError("Tabela jest pelna")
        else:
            self.T[idx] = key, val

    def insert_str(self, key, val):
        """funkcja wstawiajaca klucz string do tablicy"""
        seq = self._gen_sequence_str(key)
        flag, idx = self._search(key)
        if not flag:
            for idx in seq:
                if self._slot_is_empty(idx):
                    self.T[idx] = (key, val)
                    return None
            raise IndexError("Tabela jest pelna")
        self.T[idx] = key, val

    def insert(self, key, val):
        """funkcja wstawiajaca klucz do tablicy"""
        if type(key) == str:
            return self.insert_str(key, val)
        else:
            return self.insert_int(key, val)

    def _search(self, key):
        """funkcja wyszukujaca klucza"""
        if type(key) == int:
            seq = self._gen_sequence(key)
        else:
            seq = self._gen_sequence_str(key)
        for idx in seq:
            if self.T[idx] == None:
                return False, -1
            elif self.T[idx][0] == key:
                return True, idx
        return False, -1

    def delete(self, key):
        """funkcja usuwajaca klucz z tablicy"""
        flag, idx = self._search(key)
        if flag:
            self.T[idx] = 'Deleted'
        else:
            raise Exception("Nie ma takiego klucza")

    def get_val (self, key):
        """funkcja zwracajaca wartosc klucza"""
        ret, idx = self._search(key)
        if ret:
            return self.T[idx][1]
        else:
            raise KeyError, 'Nie ma takiego klucza'

    def __str__(self):
        """reprezentacja STR obiektu HashTable"""
        ret = "{"
        for val in self.T:
            print val
            if val is not None and val is not 'Deleted':
                ret += str(val[0]) + ': ' + str(val[1]) + ', '
        return ret[:-2] + '}'

def test():
    ht = HashTable(11)
    ht.insert(123,1)
    ht.insert("test","value")
    print ht
    ht.insert("test","value2")
    print ht
    ht.delete("test")
    print ht
    print ht.T
    

test()

ht = HashTable(11)
ht.insert(123,1)
ht.insert("test","value")
print ht
ht.insert("test","value2")
print ht
ht.delete("test")
print ht
print ht.T
ht
