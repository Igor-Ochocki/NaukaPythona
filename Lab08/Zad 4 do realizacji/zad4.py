# 4. Zapisujemy do pliku kąt w stopniach, sinus i cosinus z przedziału 0,360 co 1 stopień
# oraz czytamy dane z pliku o nazwie result_sin.tsv. Dane rozdzielamy tabulatorem \t
# Jeśli plik istnieje do kasujemy jego zawartość.
# Przy odczycie stosujemy różne sposoby formatowania łańcucha znaków ( %, .format() oraz f'),
# ale efekt wyświetlania danych ma być taki sam.
import math


with open("result_sin.tsv", "w") as dane:
    for i in range(0,361):
        dane.write(f"{i} {math.sin(math.radians(i))} {math.cos(math.radians(i))}\t")

#PI = PId 2PIr -> 2PI = 360stopni
