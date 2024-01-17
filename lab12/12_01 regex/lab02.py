# Sprawdź czy adres email jest poprawny.
# Sprawdzić czy email postaci student@p.lodz.pl oraz student@p..pl
# jest poprawny (jeśli nie, to poprawić wyrażenie regularne)
import re

# email = 'student@p..pl'
email = input('Podaj emaila: ')
# wynik = re.match(r'^[A-Z0-9._+%-.]+@[A-Z0-9-]+\.[A-Z]{2,}$', email, re.IGNORECASE)
# email = re.sub(r'\.+', '.', email)
# # wynik = re.match(r'[A-Za-z0-9]+[.-_-]+[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email, re.IGNORECASE)
# wynik = re.match(r'[A-Z0-9._-]+@[A-Z0-9-]+\.[A-Z]{2,}', email, re.IGNORECASE)
wynik = re.fullmatch(r'[A-Z0-9._-]+@([A-Z0-9]+\.)+[A-Z]{2,3}', email, re.IGNORECASE)

if wynik:
    print('Ok')
    print(wynik.group())
else:
    print('No')
