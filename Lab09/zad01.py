# 1. Wyświetlamy, każdą kolumnę i wartości w kolumnie występujące w pliku california1.txt.
# Całość zapisujemy do pliku california.csv jako plik tekstowy z separatorem średnik ';'.
# Jaka jest populacja ludzi we wszystkich miastach w przedziale wieku 18 - 64 lata
# i jaki to procent wszystkich ludzi. Plik california1.txt jest taki sam jak pobrany w poprzednich zajęciach.

with open("california1.txt", "r") as file:
    columns = []
    for line in file.readlines():
        line = line.strip()
        spliited_line = line.split(" ")
        if len(columns) == 0:
            spliited_line = line.split(",")
            columns = [[] for i in range(len(spliited_line))]
        corrected_line = []
        for i in spliited_line:
            if i != "":
                corrected_line.append(i)
        final_line = []
        city = ""
        for i in range(0,len(corrected_line)):
            if i < len(corrected_line) - 5:
                city += corrected_line[i] + " "
            elif i == len(corrected_line) - 5:
                final_line.append(city.strip())
                final_line.append(corrected_line[i].strip())
            else:
                final_line.append(corrected_line[i].strip())

        for i in range(0, len(final_line)):
            columns[i].append(final_line[i].strip())

    with open("california1.csv", "w") as save:
        for col in columns:
            for data in col :
                save.write(f"{data};")
            save.write("\n")
    populacja_od_18_do_64 = 0
    populacja = 0
    for i in range(1, len(col[0])):
        populacja += int(columns[1][i])
        populacja_od_18_do_64 += int(int(columns[1][i]) * float((columns[3][i])) / 100)
    print(columns)
    print(f"Populacja od 18 do 64 : {populacja_od_18_do_64} wynosi {(populacja_od_18_do_64/populacja)*100}% z całej populacji")