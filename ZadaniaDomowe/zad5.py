# Napisz program który posłuży do gry w zgadywanie liczby z komputerem
# Na początku podajemy zakres w którym mamy grać, następnie wybieramy liczbę z tego zakresu
# Program ma przyjmować trzy polecenia : Większe, mniejsze, równe, dowolnie opisane
# Program ma odgadnąć wybraną przez nas liczbę

# bonus : implementacja binary searcha żeby zminimalizować ilość prób programu

from random import randint

dolny_zakres = int(input("Podaj dolny zakres: "))
górny_zakres = int(input("Podaj górny zakres: "))
ilosc_zgad = 0
propozycja = randint(dolny_zakres, górny_zakres)
while propozycja != cel:
    if propozycja > cel:
        print(f"{propozycja} - Za dużo")
        propozycja = randint(dolny_zakres, górny_zakres)
        ilosc_zgad += 1
    elif propozycja < cel:
        print(f"{propozycja} - Za mało")
        propozycja = randint(dolny_zakres, górny_zakres)
        ilosc_zgad += 1
    else:
        ilosc_zgad += 1
        print(f"liczba {cel} została odgadnięta po {ilosc_zgad} próbach")
        break
    cel = int(input("Podaj zgadywaną liczbę, która jest w zakresie: "))

