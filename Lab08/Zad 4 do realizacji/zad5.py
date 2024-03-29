# 5. Czytanie danych z internetu z pliku tekstowego (wykorzystać moduł urllib.request)
# i wyświetlamy w programie tylko pierwszych 10 linii.
# Plik znajduje się w lokalizacji (jeśli nie można odnaleźć tego pliku to poszukać inny plik w prtalu kaggle.com):
# https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv

# Dodatkowo proszę poszukać plik w sieci o adresie
# 'https://imsi.p.lodz.pl/o-instytucie/pracownicy-instytutu'
# i znaleźć w nim string 'Dyrekcja Instytutu Mechatroniki i Systemów Informatycznych' i wyświetlić cały wiersz z tym stringiem.

import urllib.request

with urllib.request.urlopen("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv") as response:
    for i in range(10):
        print(response.readline().decode())

with urllib.request.urlopen("https://imsi.p.lodz.pl/o-instytucie/pracownicy-instytutu") as response:
    #print(response.read().decode())
    for line in response.read().decode():
        if 'Dyrekcja Instytutu Mechatroniki i Systemów Informatycznych' in line:
            print(line)
