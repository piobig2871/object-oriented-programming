from src.objects.fraction import Fraction


def test(fr1, fr2):
    return fr1 + fr2


b = Fraction(9, 5)
c = Fraction(1, 31)
print(test(b, c))
