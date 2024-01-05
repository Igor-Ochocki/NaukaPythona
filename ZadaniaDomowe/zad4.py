# Napisz system który pozwoli na dodawanie ocen dla uczniów, a na koniec działania programu wyliczy średnią dla każdego
# z nich.
# System ma działać lokalnie (nie wczytujemy żadnych danych, nie zapisujemy)
# Uczniowie indeksowani są numerami z dziennika (przyjmujemy że są unikalne dla każdego z nich)
# Dla każdego powtórzenia programu, program wypisuje obecną strukturę dziennika ocen, a także pyta czy chcemy dodać kolejne
# Jeśli tak, pyta najpierw dla jakiego ucznia (numer), a następnie o ocenę
# Na koniec wypisujemy strukturę dziennika i średnią dla każdego ucznia



# bonus : pytanie o ocenę do momentu wyboru innego ucznia (czyli możemy dodawać kilka ocen do ucznia na raz,
# może to być zarówno poprzez wpisanie ocen oddzielonych spacją, jak i ponowne zapytanie czy chcesz dodać ocenę dla tego ucznia)

import statistics as st

dziennik = {}

uczniowie = int(input("Podaj ilość uczniów: "))
czy = 0
for i in range(1, uczniowie + 1):
    oceny = input(f"Podaj oceny dla ucznia nr. {i} ")
    dziennik[i] = oceny.split()
print(dziennik)
pytanie = input("Czy chcesz dodać kolejne oceny? ").lower()
while pytanie == 'tak':
    nr = int(input("Podaj dla którego ucznia chcesz dodać ocene: "))
    dod = int(input(f"Podaj jaką ocene chcesz dodać dla ucznia nr.{nr}: "))
    if nr in dziennik:
        dziennik[nr].append(dod)
        print(dziennik)
    else:
        dziennik[nr] = [dod]
        print(dziennik)
    pytanie = input("Czy chcesz dodać kolejne oceny? ").lower()
print(f"Końcowy dziennik wygląda następująco: {dziennik}")



sum = 0
for key in dziennik.keys():
    for value in dziennik[key]:
        sum += int(value)
    print(f"Uczeń {key} ma średnią {sum/len(dziennik[key])}")


# Nie umiałem dokonczyc sredniej dla kazdego ucznia






