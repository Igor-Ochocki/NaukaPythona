# Napisz przykładowy kod z obsługą błędów przy odwoływaniu się do indeksu listy poza zakresem

lista = [1, 7, 4, 11, 12]

try:
    zm = lista[5]
except IndexError as e:
    print("Lista nie ma tyle elementów", e)