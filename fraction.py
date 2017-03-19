#coding: utf-8

class Ulamek(object):
    def __init__(self, licznik, mianownik):
        assert mianownik != 0, 'Mianownik musi byc rozny od 0'
        max_, min_ = (licznik, mianownik) if licznik > mianownik else (mianownik, licznik)
        self.licznik = licznik // min_ if max_ % min_ == 0 else licznik
        self.mianownik = mianownik // min_ if max_ % min_ == 0 else mianownik

    def _nwd(self, a, b):
        return b if a == 0 else self._nwd(b % a, a)

    @property
    def get_val(self):
        return self.licznik, self.mianownik

    def __repr__(self):
        return '{cls_name}({licznik}, {mianownik})'.format(cls_name= self.__class__.__name__,
                                                          licznik = self.licznik,
                                                          mianownik = self.mianownik)

    def __add__(self, other):

        if isinstance(other, Ulamek):

            nwd = self._nwd(self.mianownik, other.mianownik)
            sm, sl = self.mianownik, self.licznik
            om, ol = other.mianownik, other.licznik
            if nwd == 1:
                mianownik = sm * om
                licznik = sl * (mianownik / sm) + \
                          ol * (mianownik / om)

                return Ulamek(licznik, mianownik)

            max_, min_ = (sm, om) if sm > om else (om, sm)
            mul = max_ // min_
            if om == min_:

                return Ulamek(ol * mul + sl, sm)
            else:
                return Ulamek(sl * mul + ol, om)

        return self + Ulamek(other, 1)

    def evaluate(self):
        return self.licznik / self.mianownik


b = Ulamek(9, 5)
c = Ulamek(1, 31)
print(b + c)
