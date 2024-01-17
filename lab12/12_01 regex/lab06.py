# Napisz wyrażenie regularne do sprawdzania
# czy dana liczba jest liczbą ósemkową czy szesnastkową (tylko pełne dopasowanie)
# Dana liczba może być zarówno liczbą ósemkową i szesnastkową.
# Podaj ich odpowiednik dziesiętny.
# 0o17612
import re

regex_oct = r'^[0-7]+$'
regex_hex = r'^[0-9ABCDEF]+$'

value = input("Podaj liczbe: ")
wynik_oct = re.fullmatch(regex_oct, value)
wynik_hex = re.fullmatch(regex_hex, value, re.IGNORECASE)

if wynik_oct:
    print("Liczba może być ósemkowa, jej odpowiednik to: ", int(value, base=8))
if wynik_hex:
    print("Liczba może być szesnastkowa, jej odpowiednik to: ", int(value, base=16))
