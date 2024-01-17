# 3. Zdefiniować klasę Calculator
# (Standardowy + - * / opcja zapamiętywania oraz kasowania wyniku)
# metody add(self, amount), subtract(self, amount), multiply(self, amount), division(self, amount).
# Gdzie amount wartość, która jest np. dodawana do wartości w pamięci current.

# Następnie zdefiniować klasę ScientificCalculator, która dziedziczy po klasie Calculator
# Zawiera metody pierwiastek_kwadratowy, zamiana radiany na kąty i odwrotnie oraz sin i cos

class Calculator():
    def __init__(self):
        self.current = 0

    def add(self, amount):
        self.current += amount

    def subtract(self, amount):
        self.current -= amount

    def multiply(self, amount):
        self.current *= amount

    def division(self, amount):
        try:
            self.current /= amount
        except ZeroDivisionError:
            print("Dzielenie przez zero jest niewykonalne")

    def __add__(self, other):
        self.current += other.current

class ScientificCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def pierwiastek_kwadratowy(self):
        pass

    def rad_to_deg(self, amount):
        pass

    def deg_to_rad(self, amount):
        pass

    def sin(self, angle):
        pass
    #angle -> radians
    def cos(self, angle):
        pass

if __name__=='__main__':
    c1 = Calculator()
    c1.add(2)
    print(c1.current)
    c1.add(3)
    print(c1.current)

    c2 = Calculator()
    c2.add(4)
    print(c2.current)
    c2.add(6)
    print(c2.current)

    c1.multiply(7)
    print(c1.current)
    c2.division(3)
    print(c2.current)
    c1+c2
    print(c1.current)
