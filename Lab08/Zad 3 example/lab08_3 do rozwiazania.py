# 8.3. Dla pliku dane.dat obliczyć sumaryczny czas ruchu,
# sumaryczną przebytą drogę oraz prędkość średnią. sumaryczny - średnia
from statistics import *


movement_time = []
route = []
speed = []

with open("dane.dat", "r") as f:
    for line in f:
        # line -> każda kolejna linijka jako ciąg znaków
        # line.split() -> zwraca listę która ma elementy line podzielone po spacji // lub znaku który podamy
        # ["1.251327", "1.0247305", "0.000000"]
        if line[0] == "#": continue
        data = [float(val) for val in line.split()]
        # data = []
        # lines = line.split();
        # print(lines)
        # for val in lines:
        #     print(val)
        #     data.append(float(val))
        movement_time.append(data[0])
        route.append(data[1])
        speed.append(data[2])

print(mean(movement_time))
print(mean(route))
print(mean(speed))
