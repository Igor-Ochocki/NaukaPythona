# Napisz funkcję która przyjmuje listę liczb całkowitych oraz liczbę jako parametry, która wypisuje pierwszą napotkaną
# w liście parę taką, że suma liczb z pary jest równa liczbie przekazanej do funkcji liczba
# funkcja find_compliment
# postaraj się napisać ją w złożoności czasowej O(N) - tylko raz iterować po liście
# dodatkowo możesz zoptymalizować ją pamięciowo


def find_compliment(list, number):
    found = []
    compliments = {}

    for i in range(0, len(list) - 1):
        if (number - list[i]) in compliments:
            print(f"Pary liczb: {list[i]} {number - list[i]}")
            break
        compliments[list[i]] = 0

    print("Lista: ", list)
    print(f"Pary liczb których suma odpowiada {number} to {found}")


list = []

max = int(input("Podaj liczbę elementów w tablicy: "))

number = int(input("Podaj szukaną liczbe: "))
print("Podaj liczby: ")
for i in range(0, max):
    a = int(input(""))
    list.append(a)
find_compliment(list, number)
