# 1. Dana jest lista:
lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 16, 256, 3, 19, 71, 21]
# Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej.
# Takich par liczb może być wiele

# for i in lista:

for i in range(0, len(lista) - 1):
    if lista[i]**2 == lista[i+1]:
        print(f"Para: {lista[i]} {lista[i+1]}\n")
