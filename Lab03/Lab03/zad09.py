# zdanie dodatkowe dla chętnych - nieobowiązkowe
# ----------------------------------------------
# 9. Dwie osoby grają w oczko dwoma kostkami (do 21). 
#    Najpierw rzuca kilka razy pierwsza osoba, aż do decyzji o przerwaniu dalszych rzutów 
#    w danej partii lub przekroczeniu wartości 21 (automatyczna przegrana), a następnie rzuca druga osoba.
#   Po każdej partii:
# - wyświetlamy informację o wygranej (jednej z osób, remisie lub przegranej) obu. Podajemy wyrzucony wynik każdej z osób.
# Po zakończeniu partii:
# - liczymy ile zabrakło każdej z osób osobno do 21 (sumujemy ilość gier) - liczymy średnią,
# - liczymy ile było było wartości 21 dla kazdej z osób (sumujemy ilość gier),
# - liczymy o ile przekroczyła każda z osób wartość 21 (sumujemy ilość gier przegranych) - liczymy średnią.

# Aby skasowac historię rzutów danej osoby należy wyczyścić ekran consoli poleceniem:
import os

# niekończący się program (teoretycznie)
# dla każdej pętli pobrać input: ( na końcu ) czy chcesz grać ponownie?
# dla każdej partii: pobieramy input od użytkownika czy chce losować (na koniec pierwszy - zawsze)
# sumujemy jego wyniki (losujemy wartosc od 1 do 6) jak przekroczy 21 mówimy i przerywamy jego losowanie
# dla drugiego to samo
# sprawdzamy kto wygrał, kto przegrał
# jak nie chcą grać ponownie: linie 9-11 (statystyka)

from random import *

brakujace_pierwszego = 0
brakujace_drugiego = 0
ile_21_pierwszego = 0
ile_21_drugiego = 0
suma_gier = 0
przekroczone_pierwszego = 0
przekroczone_drugiego = 0
ilosc_przekroczona_pierwszego = 0
ilosc_przekroczona_drugiego = 0

while True:
    suma_gier += 1
    suma_pierwszego = 0
    while True:
        rzut_1 = randint(1, 6)
        rzut_2 = randint(1, 6)
        suma_pierwszego += rzut_1 + rzut_2
        print("Wyrzucona wartość: ", suma_pierwszego)
        if suma_pierwszego > 21:
            przekroczone_pierwszego += 1
            ilosc_przekroczona_pierwszego += abs(21 - suma_pierwszego)
            print("Przegrana gracza pierwszego (ponad 21)", suma_pierwszego)
            print("Wygrana gracza drugiego")
            break
        decyzja = input("Czy chcesz rzucać dalej? (TAK / NIE): ")
        if decyzja != "TAK":
            break
    brakujace_pierwszego += abs(21 - suma_pierwszego)
    suma_drugiego = 0
    if suma_pierwszego == 21:
        ile_21_pierwszego += 1
    if suma_pierwszego <= 21:
        while True:
            rzut_1 = randint(1, 6)
            rzut_2 = randint(1, 6)
            suma_drugiego += rzut_1 + rzut_2
            print("Wyrzucona wartość: ", suma_drugiego)
            if suma_drugiego > 21:
                przekroczone_drugiego += 1
                ilosc_przekroczona_drugiego += abs(21 - suma_drugiego)
                print("Przegrana gracza drugiego (ponad 21)", suma_drugiego)
                print("Wygrana gracza pierwszego")
                break
            decyzja = input("Czy chcesz rzucać dalej? (TAK / NIE): ")
            if decyzja != "TAK":
                break
    brakujace_drugiego += abs(21 - suma_drugiego)
    if suma_drugiego == 21:
        ile_21_drugiego += 1
    if suma_pierwszego <= 21 and suma_drugiego <= 21:
        if suma_pierwszego > suma_drugiego:
            print("Gracz pierwszy wygrał\n Pierwszy gracz:", suma_pierwszego, "\nDrugi gracz:", suma_drugiego)
        elif suma_drugiego > suma_pierwszego:
            print("Gracz drugi wygrał\n Pierwszy gracz:", suma_pierwszego, "\nDrugi gracz:", suma_drugiego)
        else:
            print("Remis\n Pierwszy gracz:", suma_pierwszego, "\nDrugi gracz:", suma_drugiego)
    if input("Czy chcecie grać dalej? (TAK / NIE)") != "TAK":
        break
    os.system('cls')
print("Graczowi pierwszemu zabrakło do 21 średnio", brakujace_pierwszego / suma_gier)
print("Graczowi drugiemu zabrakło do 21 średnio", brakujace_drugiego / suma_gier)
print("Gracz pierwszy wylosował 21", ile_21_pierwszego, "razy")
print("Gracz drugi wylosował 21", ile_21_drugiego, "razy")

