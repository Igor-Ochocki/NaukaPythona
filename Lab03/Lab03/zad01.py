# 1. Sprawdź czy podana liczba jest parzysta czy nieparzysta 
#    (definiujemy funkcję is_even(a), która zwraca True lub False (typ bool))
#    W pliku zad01.py dodajemy w kodzie w odpowiednim miejscu sprawdzenie 
#    czy    if __name__ == '__main__':     w celu uruchomienia zdefiniowanej wcześniej funkcji. 
#    Proszę także zaimportować bibliotekę math poleceniem : from math import *

from math import *
def is_even(a):
    return a % 2 == 0


if __name__ == '__main__':
    liczba = int(input("Podaj liczbę: "))
    print("Liczba parzysta" if is_even(liczba) else "Liczba nieparzysta")
