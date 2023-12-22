#app03
#Wyświetl n kolejnych liczb (instrukcja while)
#Liczbę n podajemy z klawiatury. Pierwsza liczba jest 1.
#Sprawdź na końcu działanie funkcji vars()
# [klucz, wartość] -> [key, value]
print(vars())
v = {
    0: [0, 1, 3],
    1: 3,
    "1": "1"
}

class Samochod:
    silnik = "1.0"
    przebieg = 25000

# liczby 1 .. n
n = 2
#n = int(input("Podaj liczbę całkowitą: "))
i = 1
while i <= n:
    print(i)
    i += 1

#v.values() -> key?
print("------------")
for key in v.keys():
    print(str(key) + " " + str(v[key]))

for x in v:
    print(x)