# Napisz przykładowy kod z obsługą błędów przy otwieraniu pliku do odczytu, który nie istnieje.

try:
    f = open("test.txt", "r")
except FileNotFoundError as e:
    print("Wystąpił błąd: ", e)