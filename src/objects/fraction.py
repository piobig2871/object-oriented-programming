# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class Fraction(object):
    def __init__(self, nominator, denominator):
        assert denominator != 0, 'Denominator must be different than zero!'
        max_, min_ = (nominator, denominator) if nominator > denominator else (denominator, nominator)
        self.nominator = nominator // min_ if max_ % min_ == 0 else nominator
        self.denominator = denominator // min_ if max_ % min_ == 0 else denominator

    def _nwd(self, a, b):
        return b if a == 0 else self._nwd(b % a, a)

    @property
    def get_val(self):
        return self.nominator, self.denominator

    def __repr__(self):
        return f'{self.__class__.__name__}({self.nominator}, {self.denominator})'

    def __add__(self, other):
        if isinstance(other, Fraction):

            nwd = self._nwd(self.denominator, other.denominator)
            sm, sl = self.denominator, self.nominator
            om, ol = other.denominator, other.nominator
            if nwd == 1:
                denominator = sm * om
                nominator = sl * (denominator / sm) + ol * (denominator / om)

                return Fraction(nominator, denominator)

            max_, min_ = (sm, om) if sm > om else (om, sm)
            mul = max_ // min_
            if om == min_:

                return Fraction(ol * mul + sl, sm)
            else:
                return Fraction(sl * mul + ol, om)

        return self + Fraction(other, 1)

    def evaluate(self):
        return self.nominator / self.denominator
