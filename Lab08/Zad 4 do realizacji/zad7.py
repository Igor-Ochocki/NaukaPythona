# 7. Mamy plik tekstowy z danymi medycznymi msk_impact_2017_clinical_data.tsv
# Należy podać ile jest w danym pliku linii (wierszy bez wiersza nagłówkowego).
# Następnie wyświetlić te wiersze, które mają największą liczbę znaków z wyłączeniem białych znaków.
import string

with open("msk_impact_2017_clinical_data.tsv", "r") as data:
    lines = data.readlines()[1:]
    print(f"Linie w pliku: {len(lines)}")
    max_characters = -1
    max_character_lines = []
    for line in lines:
        for whitespace in string.whitespace:
            line = line.replace(whitespace, "") # usuwamy wszystkie białe znaki z linii

        if len(line) > max_characters:
            max_characters = len(line)
            max_character_lines = [line]
        if len(line) == max_characters:
            max_character_lines.append(line)
    for line in max_character_lines:
        print(line)