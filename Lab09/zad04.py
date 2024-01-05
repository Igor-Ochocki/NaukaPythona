# 4. Wykorzystć moduł pickle do zapisania w pliku dane.dat
# wygenerowanych 10000 liczb całkowitych o wartości od 0 do 100.
# Następnie czytamy dane z tego pliku i szukamy, które z wygenerowanych liczb jest najwięcej.
import pickle
from random import *


numbers = []
for i in range(10000):
    numbers.append(randint(0, 100))
pickle.dump(numbers, open("dane.dat", "wb") )
file = pickle.load(open("dane.dat", "rb"))
count = {}
for number in file:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1
max_numbers = []
max_number_count = 0
for number in count:
    if count[number] > max_number_count:
        max_number_count = count[number]
        max_numbers = [number]
    elif count[number] == max_number_count:
        max_numbers.append(number)
print(file)
print(max_numbers)