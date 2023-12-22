# app02
# Do zadania numer 1 dodajemy wyświetlanie typu zmiennej a,b,c (funkcja type())
# Sprawdź jak działa funkcja isinstance() do sprawdzenia i wyświetlenia typu danych danej zmiennej.

a = float(input("Podaj A: "))

b = float(input("Podaj B: "))

c = a + b

print(c)

if(isinstance(a, (float))):
    print("A to float")

print("Typ zmiennej A: " + str(isinstance(a, (float, int, str))))
print("Typ zmiennej B: " + str(type(b)))
print("Typ zmiennej C: " + str(type(c)))