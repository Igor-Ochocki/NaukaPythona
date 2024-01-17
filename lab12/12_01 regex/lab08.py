# Napisz wyrażenie regularne do sprawdzenia czy podany czas
# w formacie hh:min:sec.100sec jest poprawny (tylko pełne dopasowanie)

# ([01]\d|2[0-3]) -> ( 0(0-9) v 1(0-9) ) v 2(0-3)
import re

czas = input('Podaj czas w formacie (hh:min:sec.100sec):\n')

wynik = re.match(r'^(([01]\d|2[0-3])(:([0-5]\d)){2}[.]\d{3})$', czas)

if wynik:
    print(czas)
else:
    print("Nieprawidłowy format")
