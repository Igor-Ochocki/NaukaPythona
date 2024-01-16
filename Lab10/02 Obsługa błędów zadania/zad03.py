# Napisz przykładowy kod z obsługą błędów przy odczycie ze słownika nieistniejącego klucza

dictionary = {
    "kot": 12,
    "cebula": 7
}

try:
    dictionary["pies"]
except KeyError as error:
    print("Klucz nie istnieje w słowniku: ", error)