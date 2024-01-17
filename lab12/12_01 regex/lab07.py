# Napisz definicję funkcji is_valid_license_plate(license_plate)
# z wykorzystaniem wyrażenia regularnego do sprawdzenia poprawnoścci
# tablic rejestracyjnych z Łodzi np. EL 45JK3.
# Funkcja zwraca True lub False.

import re


def is_valid_license_plate(license_plate):
    wynik = re.match(r'^EL\s[A-Z0-9]{4,5}$', license_plate)

    if wynik:
        return True
    else:
        return False


if __name__ == '__main__':
    tablica = input('Podaj tablice: ')
    result = is_valid_license_plate(tablica)
    print(result)
