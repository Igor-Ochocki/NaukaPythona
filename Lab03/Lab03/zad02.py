# 2. Oblicz sumę liczb parzystych tworząc funkcję sum_even(a,b) z przedziału podanego jako parametry funkcji 
#   (korzystamy z funkcji is_even(a) z zadania zad01.py, która zwraca True lub False 
#   - wykorzystujemy instrukcję from zad01 import * albo import zad01).
#   następnie definiujemy funkcję sum_odd(a,b) do obliczania sumy liczb nieparzystych.
from zad01 import *


def sum_even(a, b):
    suma = 0
    for i in range(a, b+1):
        if is_even(i):
            suma += i
    return suma


def sum_odd(a, b):
    if a > b:
        a, b = b, a
    suma = 0
    for i in range(a, b+1):
        if not is_even(i):
            suma += i
    return suma


if __name__ == '__main__':
    b = int(input("Podaj górny zakres: "))
    a = int(input("Podaj dolny zakres: "))
    print(sum_odd(a, b))