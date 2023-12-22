# 1. Rozwiązywanie równania kwadratowego w dziedzinie liczb urojonych (zespolonych)
#    definiujemy funkcje quadratic_equation_im(a,b,c) zwracjące listę w postaci [x1, x2]
#    Podać przykład uruchomienia funkcji.

from math import *


a: int = int(input("Podaj współczynnik przy x^2 równania: "))
b = int(input("Podaj współczynnik przy x równania: "))
c = int(input("Podaj wartość wyrazu wolnego równania: "))


def quadratic_equation(a, b, c):
    delta = b**2 - 4 * a * c
    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        return [x1, x2]
    if delta == 0:
        x = (-b)/(2*a)
        return [x, ""]
    if delta < 0:
        x = -b / (2 * a)
        x_i = sqrt(-delta) / (2 * a)
        x1 = "{}-{}i".format(x, x_i)
        x2 = "{}+{}i".format(x, x_i)
        return [x1, x2]


result = quadratic_equation(a, b, c)
print("Rozwiązania", result[0], result[1])