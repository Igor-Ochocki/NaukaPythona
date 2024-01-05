# 3. Czytamy wszystkei dane z pliku cereals.csv (wykorzystać moduł csv)
# Dodajemy do pliku cereals.csv na końcu jednego wiersza z dowolnymi danymi.
# np. "Miodek","G ","C ",100,4,2,340,1,16,8,60,25,1,1,0.75,3.755922,1,0,0,0,1,0,0

import csv

with open("cereals.csv", 'a', newline='') as csvfile:
    write_file = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    write_file.writerow(["Miodek","G ","C ",100,4,2,340,1,16,8,60,25,1,1,0.75,3.755922,1,0,0,0,1,0,0])