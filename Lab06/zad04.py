# 4. Wykorzystując moduł time i funkcję time obliczyć ile trwa pętla
#    składająca się z 100000 iteracji dla listy i dla typu tuple (np. sumowanie).
import time
from time import *
lista = [7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21]
krotka = (7, 49, 3, 9, 18, 6, 5, 25, 24, 4, 4, 5, 3, 19, 71, 21)

init_time = time()
for i in range(10000000):
    sum(krotka)
print(f"{init_time - time()}")
init_time = time()
for i in range(10000000):
    sum(lista)
print(f"{init_time - time()}")
