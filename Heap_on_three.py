class TriHeapMAX:
    def __init__(self, T):
        self.hSize = len(T) - 1
        self.heap = T
        self._build_max_heap(self.heap)

    def _parent(self, i):
    ## Wyznacz rodzica
        return (i - 1) / 3

    def _left(self, i):
    ## Wyznacz lewe dziecko
        return i * 3 + 1

    def _middle(self, i):
    ## Wyznacz srodkowe dziecko
        return i * 3 + 2

    def _right(self, i):
    ## Wyznacz prawe dziecko
        return i * 3 + 3

    def _fix_down(self, i):
    ## Napraw wlasnosc kopca w dol
        l = self._left(i)
        m = self._middle(i)
        r = self._right(i)

        if l <= self.hSize:
            if self.heap[l] > self.heap[i]:
                largest = l
            else:
                largest = i
        else:
            largest = i

        if m <= self.hSize:
            if self.heap[m] > self.heap[largest]:
                largest = m

        if r <= self.hSize:
            if self.heap[r] > self.heap[largest]:
                largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._fix_down(largest)

    def _fix_up(self, i):
    ## Napraw wlasnosc kopca w gore
        while i > 1 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _build_max_heap(self, T):
    ## Stworz kopiec z listy
        for i in range(self.hSize / 3, -1, -1):
            self._fix_down(i)

    def extract_max(self):
    ## Zwroc maksimum kopca
        if self.hSize > 0:
            maxi = self.heap[0]
            self.heap[0] = self.heap[self.hSize - 1]
            self.hSize -= 1
            self._fix_down(0)
            return maxi
        else:
            return None

    def increase_key(self, i, key):
        if key < self.heap[i]:
            return None
        self.heap[i] = key
        self._fix_up(i)

    def insert(self, key):
        self.hSize += 1
        self.heap.insert(self.hSize - 1, -999999)
        self.increase_key(self.hSize - 1, key)

    def sort(self):
        ret = []
        while self.hSize > 0:
            ret.insert(0, self.extract_max())
        return ret
            

L = [71,66,24,32,27,23,8,5,22,25,18]
test = TriHeapMAX(L)
print test.sort()
        
