# 1. Podaj listę z pocztą elektroniczną kilku użytkowników i wylosuj jeden z nich.
data = ['user3@gmail.com','user2@gmail.com','user2@interia.com','user1@gmail.com','user1@interia.com']
# W ramach tej samej listy wybierz do losowania tylko adresy z poczty gmail.com i wylosuj jeden z nich.
from random import *


print(data[randint(0, len(data)-1)])

#data2 = [item for item in data if "gmail.com" in item]
data2 = []
for item in data:
    if "gmail.com" in item:
        data2.append(item)
print(data2[randint(0, len(data2)-1)])