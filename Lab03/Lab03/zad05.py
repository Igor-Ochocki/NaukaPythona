# 5. Sprawdź czy podana liczba jest liczbą pierwszą i zdefiniuj funkcję is_prime(a) zwracjącą wartość True lub False. 
#    - wymyślamy swój algorytm niekoniecznie optymalny 
#    - (2 jest liczbą pierwszą, liczby mniejsze od 2 nie są liczbami pierwszymi, liczby większe od 2 - zależy od liczby)
# 15 liczba pierwsza <=> nie / 2,3,4,5,6,7,...,14
from math import *


def is_prime(a):
    for i in range(2, int(sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


if __name__ == '__main__':
    liczba = int(input("Podaj liczbę: "))
    print("Liczba pierwsza" if is_prime(liczba) else "Liczba nie jest liczbą pierwszą")
