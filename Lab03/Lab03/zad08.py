# 8. Rozwiązywanie równania kwadratowego w dziedzinie liczb rzeczywistych
#    - rozwiązanie tworzymy na początku bez funkcji (kod bez definiowania funkcji) 
#
#    - Następnie docelowo definiujemy funkcje quadratic_equation(a,b,c) zwracjące listę 
#    w postaci [x1, x2, 'komentarz ile jest rozwiązań']
#    Podać przykład uruchomienia funkcji, gdzie mamy jedno rozwiązanie, 2 rozwiązania lub brak rozwiązania.
from math import *


a: int = int(input("Podaj współczynnik przy x^2 równania: "))
b = int(input("Podaj współczynnik przy x równania: "))
c = int(input("Podaj wartość wyrazu wolnego równania: "))


def quadratic_equation(a, b, c):
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        return [x1, x2, "Dwa rozwiązania: "]
    if delta == 0:
        x = (-b)/(2*a)
        return [x, "", "Jedno rozwiązanie: "]
    if delta < 0:
        return ["", "", "Brak rozwiązań"]


result = quadratic_equation(a,b,c)
print(result[2], result[0], result[1])
