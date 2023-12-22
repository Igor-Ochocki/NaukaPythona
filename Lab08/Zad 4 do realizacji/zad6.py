# 6. Napisać funkcję find_word(filename_input, word),
# której zadaniem jest znalezienie wszystkich wierszy w pliku filename_in.txt, które zawierają szukane słowo.
# Wszystkie wiersze, które zawierają dane słowo powinny zostać zapisane w pliku wynikowym filnename_out.txt
# wraz z nr wiersza (z pierwszego pliku). Plik wejściowy to dowolny plik tekstowy.


def find_word(filename_input, word):
    result = open(f"{filename_input}_out.txt", "w")
    with open(f"{filename_input}_in.txt", "r") as file:
        line_number = 1
        for line in file:
            if word in line:
                result.write(f"{line_number} {line}")
            line_number += 1
    result.close()

find_word("input2", "My")
