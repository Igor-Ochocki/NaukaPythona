# 2. Napisać funkcję countChar(filename_input), która zlicza:
#   - liczbę znaków w pliku,
#   - liczbę białych znaków w pliku (białe znaki to spacja, tabulator, znacznik końca wiersza),
#   Wynikiem funkcji jest tablica złożona z 2 liczb całkowitych po jednej dla wymienionych podpunktów.
import string
# (białe znaki to spacja, tabulator, znacznik końca wiersza)

def countChar(filename_input: str):
    characters = 0
    white_characters = 0
    with open(filename_input, "r") as file:
        for line in file:
            for character in line:
                characters += 1
                if character in string.whitespace:
                    print(character, end="")
                    white_characters += 1
    return [characters, white_characters]


print(countChar("dane.dat"))
