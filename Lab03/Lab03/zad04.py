# 4. Na podstawie funkcji z zadania zad03.py, tworzymy funkcję sum_all(a,b), 
#    która liczy sumę liczb parzystych i nieparzystych razem. 
#    Nie definiujemy od sumowania wszystkich liczb od początku tylko wykorzystujemy funkcję suma(typ,a,b)
#  Dodatek:
#    Na końcu zadania proszę wykonać polecenie print('Wynik =',sqrt(9)) bez importu biblioteki math. 
#    Czy polecenie działa i dlaczego mimo braku polecenia import w pliku zad04.py?

from zad03 import *

def sum_all(a, b):
    return suma(True, a, b) + suma(False, a, b)


if __name__ == '__main__':
    a = int(input("Podaj górny zakres: "))
    b = int(input("Podaj dolny zakres: "))
    print(sum_all(a, b))
    print('Wynik = ', sqrt(9))
