# coding: utf-8

from collections import Counter
from math import sqrt
import matplotlib.pyplot as plt


class Statystyka:
    def __init__(self, tablica):
        '''Klasa statystyka zwracająca podstawowe zagadnienia związane
            ze statystyką'''
        self.tablica = tablica
        for i in self.tablica:
            assert type(i) == int or type(i) == float

    def srednia_arytmetyczna(self):
        '''funkcja zwracąjaca średnią arytmetyczną liczb w podanej tablicy
            WEJSCIE:
            tablica liczb
            ______________
            WYJSCIE:
            srednia arytmetyczna (liczba typu int lub float)'''
        suma = 0
        for i in self.tablica:
            suma += i
        ret = suma / len(self.tablica)
        return ret

    def srednia_geometryczna(self):
        '''funkcja zwracajaca srednia geometryczna liczb w podanej tablicy
            WEJSCIE:
            tablica liczb
            ______________
            WYJSCIE:
            srednia geometryczna (liczba typu int lub float)'''
        n = len(self.tablica)
        iloczyn = 1
        for i in self.tablica:
            iloczyn *= i
        s_g = iloczyn ** (1 / n)
        return s_g

    def srednia_kwadratowa(self):
        '''funkcja zwracajaca srednia kwadratowa liczb w podanej tablicy
            WEJSCIE:
            tablica liczb
            ______________
            WYJSCIE:
            srednia kwadratowa (liczba typu int lub float)'''
        temp = 0
        n = len(self.tablica)
        for i in self.tablica:
            i = i ** 2
            temp += i
        s_k = sqrt(temp / n)
        return s_k

    def minimum(self):
        '''Funkcja zwracajaca minimalny element w tablicy
        WEJSCIE:
        tablica liczb
        _____________
        WYJSCIE:
        liczba typu int lub float'''
        x = 0
        mini = self.tablica[x]
        while x < len(self.tablica):
            if self.tablica[x] < mini: mini = self.tablica[x]
            x += 1
        return mini

    def maksimum(self):
        '''Funkcja zwracajaca maksymalny element w tablicy
        WEJSCIE:
        tablica liczb
        _____________
        WYJSCIE:
        liczba typu int lub float'''
        x = 0
        maks = self.tablica[x]
        while x < len(self.tablica):
            if self.tablica[x] > maks: maks = self.tablica[x]
            x += 1
        return maks

    def odchylenie_standardowe(self):
        '''Funkcja zwraca odchylenie standardowe dla liczb podanych w tablicy
        WEJSCIE:
        tablica liczb
        ________________
        WYJSCIE:
        liczba tylu int lub float'''
        wynik = self.wariancja()
        return sqrt(wynik)

    def histogram(self):
        '''funkcja zwracajaca ilosc wystapien wartosci w tablicy'''
        sl = Counter(self.tablica)
        return [list(sl.keys()), list(sl.values())]

    def wykres_słupkowy(self):
        x, y = self.histogram()
        plt.bar(x, y, color='c')
        plt.xlabel('dziedzina')
        plt.ylabel('zbiór wartości')
        plt.title('wykres słupkowy')
        plt.show()

    def wariancja(self):
        '''Funkcja zwraca wariancje dla liczb podanych w tablicy
        WEJSCIE:
        tablica liczb
        ________________
        WYJSCIE:
        liczba tylu int lub float'''
        suma = 0
        dlugosc = len(self.tablica)
        s_a = self.srednia_arytmetyczna()
        a = 0
        for x in self.tablica:
            a = (x - s_a) ** 2
            suma += a
            wynik = suma / dlugosc
        return wynik

    def mediana(self):
        '''Funkcja zwraca mediane dla liczb podanych w tablicy
        WEJSCIE:
        tablica liczb
        ________________
        WYJSCIE:
        liczba typu int lub float'''
        n = len(self.tablica)
        s = self.selectionSort()
        if n % 2 == 0:
            a = n / 2 + 1
            b = n / 2 - 1
            srednia = (a + b) / 2
        else:
            srednia = n / 2
        return srednia

    def selectionSort(self):
        '''Funkcja zwraca posortowany ciag liczb, dla liczb podanych w tablicy
        WEJSCIE:
        tablica liczb
        ________________
        WYJSCIE:
        posortowana tablica liczb.'''
        for i in range(len(self.tablica) - 1, -1, -1):
            aktualne = 0
            for pozycja in range(1, i + 1):
                if self.tablica[pozycja] >= self.tablica[aktualne]:
                    aktualne = pozycja
            buf = self.tablica[i]
            self.tablica[i] = self.tablica[aktualne]
            self.tablica[aktualne] = buf
        return buf

    def normalizacja(self):
        '''Funkcja zwraca wstępną obróbkę danych w celu umożliwienia ich porównywania i dalszej analizy.
        WEJŚCIE:
        tablica liczb
        -------------
        WYJŚCIE:
        tabclica znormalizowana.
        '''
        ret = []
        xij = 0
        avg = self.srednia_arytmetyczna()
        odc = self.odchylenie_standardowe()
        for val in self.tablica:
            xij = float(val - avg) / odc
            ret.append(xij)
        return ret

    def skalownaie_liniowe_skalar(self, skalar):
        '''Funkcja mnoży wektor przez skalar.
        WEJŚCIE:
        tablica liczb(wektor)
        --------------------
        WYJŚCIE:
        tablica liczb(wektor) przemnożony przez skalar.
        '''
        return list(map(lambda x: x * skalar, self.tablica))

    def wykres_liniowy(self):
        x, y = self.tablica, [self.srednia_geometryczna() for _ in range(len(self.tablica))]
        plt.plot(x, y, color='r')
        plt.xlabel('dziedzina')
        plt.ylabel('zbiór wartości')
        plt.title('wykres liniowy')
        plt.show()


a = Statystyka([3.5, 4.5, 4, 3.5, 4, 4.5, 5, 4, 4, 5])
print(a.maksimum())
print(a.minimum())
print(a.srednia_arytmetyczna())
print(a.mediana())
print(a.wariancja())
print(a.odchylenie_standardowe())
print(a.normalizacja())
print(a.mediana())
print(a.skalownaie_liniowe_skalar(3))
print(a.histogram())
print(a.wykres_słupkowy())
print(a.wykres_liniowy())
