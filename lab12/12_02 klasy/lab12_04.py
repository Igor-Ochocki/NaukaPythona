# Napisz klasę FunkcjaKwadratowa,
# która przechowuje funkcje typu ax**2+bx+c.
# Klasa powinna zawierać trzy pola: a, b, c, które są przypisywane w konstruktorze.
# Główną metodą powinna być resolve(), która zwraca miejsca zerowe podanej funkcji w dziedzinie liczb rzeczywistych.
# Należy zwrócić uwagę na przypadki, gdy a=0 (nie jest to rownanie kwadratowe) lub braku rozwiązań.
# Dodatkowo definiujemy funkcję aby wpisać całe równanie w postaci - a*x**2+b*x+c
# oraz oblicznie wartości funkcji w punkcie x.
import math


class FunkcjaKwadratowa:
    def __init__(self, a, b, c):  # konstruktor
        self.a = a
        self.b = b
        self.c = c

    def show_equation(self):
        pass  # wpisz całe równanie w postaci - a*x**2+b*x+c
        print(f"{self.a}*x**2+{self.b}*x+{self.c}")

    def calculate_value(self, x):
        return self.a * x**2 + self.b * x + self.c
        pass  # oblicz wartość funkcji w punkcie x

    def resolve(self):
        if self.a == 0:
            return "Funkcja nie jest funkcją kwadratową"
        delta = self.b**2 - 4 * self.a * self.c
        if delta < 0:
            return "Brak miejsc zerowych"
        if delta == 0:
            return (-self.b/(2*self.a))
        if delta > 0:
            return (((-self.b - math.sqrt(delta)) / (2*self.a)), ((-self.b + math.sqrt(delta)) / (2*self.a)))
          # zwróć rozwiązanie w postaci pary dwóch liczb lub komunikatu (lista lub tupla)


def main():
    fun1 = FunkcjaKwadratowa(2, 3, 11)
    fun1.show_equation()
    print(fun1.calculate_value(0))
    print(fun1.calculate_value(1))

    print(FunkcjaKwadratowa(0, 0, 0).resolve())
    print(FunkcjaKwadratowa(0, 0, 9).resolve())
    print(FunkcjaKwadratowa(0, 4, 3).resolve())
    print(FunkcjaKwadratowa(4, 2, 3).resolve())
    print(FunkcjaKwadratowa(1, 2, 1).resolve())
    print(FunkcjaKwadratowa(1, 5, 6).resolve())
    print(fun1.resolve())


if __name__ == "__main__":
    main()
