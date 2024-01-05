# 0. (zadanie z ostatnich zajęć)
# - nie kopiujemy pliku do danego katalogu, tylko próbujemy otworzyć plik z katalogu Lab08/....)
# Mamy plik tekstowy z danymi medycznymi msk_impact_2017_clinical_data.tsv
# Należy podać ile jest w danym pliku linii,
# Następnie ile jest kobiet i mężyczyzn
# (sprawdzić czy istnieją rekordy, gdzie nie pojawia się informacja jaka jest płeć - wypisać te wartości lub rekordy)
# Podać ilość precentowy kobiet i mężczyzn w tej populacji.

with open("../Lab08/Zad 4 do realizacji/msk_impact_2017_clinical_data.tsv", "r") as file:
    lines = file.readlines()
    print(f"Liczba linii: {len(lines)}")
    kobiety = 0
    mezczyzni = 0
    inne = 0
    headers = lines[0]
    idx = headers.split("\t").index("Sex")
    lines = lines[1::]
    for line in lines:
        splitted_line = line.split("\t")
        if splitted_line[idx] == "Male":
            mezczyzni += 1
        if splitted_line[idx] == "Female":
            kobiety += 1
        if splitted_line[idx] != "Male" and splitted_line[idx] != "Female":
            inne += 1
            print(splitted_line[idx])
    print(f"Procentowy udział kobiet : {kobiety*100/float((kobiety+mezczyzni))}, procentowy udział mężczyzn : {mezczyzni*100/float((kobiety+mezczyzni))}")
    print(f"W pliku wystąpiło {kobiety} kobiet i {mezczyzni} mężczyzn i {inne} innych")