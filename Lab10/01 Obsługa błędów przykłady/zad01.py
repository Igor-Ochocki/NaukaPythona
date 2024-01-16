# Obsługa wyjątków try/except

# brak obsługi wyjątków
print('------------------------------')

# obsługa wyjątków
try:
    num = 5 / 0
except:
    print("Wystąpił jakiś błąd!")
print('------------------------------')

# obsługa konkretnego wyjątku
try:
    num = 5 / 0
except ValueError:
    print("Podana zmienna nie jest liczbą !")
print('KONIEC SKRYPTU')
