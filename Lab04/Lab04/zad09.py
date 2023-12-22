# 9. Z wykładu definiujemy funkcję silnia(a)
#  i porównujemy wyniki z funkcją math.factorial().
#  Śledzimy za pomocą debugera wykonanie rekurencyjne naszej funkcji silnia.
#  Dodatkowo wykorzystujemy funkcję time() z biblioteki time do sprawdzenia,
#  które z obliczeń działa szybciej (sprawdzić dla dość dużych liczb)
import math
import time


def silnia(a):
    if a == 1:
        return 1
    else:
        return a * silnia(a - 1)

initial = time.time()
math.factorial(998)
end = time.time()
print(end - initial)
initial = time.time()
silnia(998)
end = time.time()
print(end - initial)