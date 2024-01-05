# 5. Wykorzystanie modułu shelve do zapisania rzutów dwoma kostkami,
# aż do wyrzucenia wartości 12 (zapisujemy kolejne sumy).
# Powtarzamy tą operację jeszcze 10 razy i każdą z serii zapisujemy do nowego zestawu danych.
# Następnie czytamy dane z pliku i podajemy ile rzutów potrzebujemy, w każdej serii
# do wyrzucenia sumy równej 12. Następnie liczymy jedną wartość średnią z wszystkich serii.

import shelve
from random import randint

d = shelve.open("rzuty")

for i in range(25):
    rzut = 0
    idx = 0
    throws = []
    while rzut != 12:
        rzut = randint(1,6) + randint(1,6)
        throws.append(rzut)
        idx += 1
    d[str(i)] = throws

sum = 0
for key in d.keys():
    sum += len(d[key])
    print(len(d[key]))
print(sum / len(d.keys()))

d.close()