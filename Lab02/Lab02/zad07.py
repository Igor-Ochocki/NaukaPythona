# app07
# zaimportuj moduł random poleceniem - import random
# wybierz losowo liczbę całkowitą od 0 do 100 - funkcja randint() oraz randrange() (jaka jest różnica między funkcjami)
# wybierz losowo wartość z tablicy data = ['jeden','dwa','trzy','cztery','pięć','sześć'] - funkcja choice()
# wybierz losowo liczbę od 0 do 1 - funkcja random()

import random as rnd # tożsame z #include <>

print(rnd.randint(0, 100)) # randint(a,b) -> przedział <a,b>
print(rnd.randrange(100))

data = ['jeden','dwa','trzy','cztery','pięć','sześć']
print(rnd.choice(data))

print(rnd.random())
# dla przedziału x, y (x < y)
# rnd.random(x + rnd.random() * (y - x))