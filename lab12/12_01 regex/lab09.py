# Napisz wyrażenie regularne do sprawdzenia wymagań co do hasła,
# gdzie spełnione są wszystkie poniższe warunki:
# hasło musi zawierać 1 cyfrę (0-9)
# hasło musi zawierać 1 wielką literę
# hasło musi zawierać 1 małą literę
# hasło musi zawierać 1 liczbę inną niż alfanumeryczna
# hasło składa się z 8-16 znaków bez spacji
# Przy sprawdzaniu podajemy co w kolejności od góry nie zostało jeszcze spełnione
# aż podamy hasło, które spełnia wszystkie wymogi.
# !#%&?.=@


import re
# r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*\W)\S{8,16}$'

haslo = input('Podaj hasło spełniające wszystkie wymagania: ')
regex = r'^((?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!#%&?.=@]))\S{8,16}$'
wynik = re.match(regex, haslo)

if not wynik:
    print('Haslo nie spełnia wymagan')
    if not any(char.isdigit() for char in haslo):
        print('Brak liczby')
    elif not any(char.isupper() for char in haslo):
        print('Brak duzej litery')
    elif not any(char.islower() for char in haslo):
        print('Brak małej litery')
    elif all(char.isalnum() for char in haslo):
        print('Brak liczby innej niz alfanumeryczna')
    elif ' ' in haslo:
        print('Niedozwolona spacja')
else:
    print('Haslo spelnia wymagania')


