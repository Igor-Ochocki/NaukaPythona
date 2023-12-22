# 2. Dana jest lista:
lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
# Oblicz sumę, wartość średnią, wartość minimalną i maksymalną z wykorzystaniem
# i bez korzystania z funkcji wbudowanych sum, min, max, len.

print(f"Suma: {sum(lista)}\nŚrednia: {sum(lista)/len(lista)}\nMin: {min(lista)}\nMax: {max(lista)}")

suma = 0
mini = lista[0]
maxi = lista[0]
elem = 0

for i in lista:
    elem += 1
    suma += i
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print("================================")
print(f"Suma: {suma}\nŚrednia: {suma/elem}\nMin: {mini}\nMax: {maxi}")
