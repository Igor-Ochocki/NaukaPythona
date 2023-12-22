# 9. Zapropnuj słownik lub listę do sprawdzenia oceny w zależności od liczby punktów
# podanej z klawiatury (do wyboru oceny od 2-5 stosujemy słownik lub listę)
# Jeżeli zmienią się zakresy na liście lub oceny to także wynik końcowy może być inny.
# 	5 - (80%-100%>
# 	4 - (60%-80%>
# 	3 - (50-60%>
# 	2 - <=50%>

dictionary = {
    5: [80, 100],
    4: [60, 80],
    3: [50, 60],
    2: [0, 50]
}

wynik = int(input("Podaj wynik w procentach: "))
for key in dictionary:
    if dictionary[key][0] < wynik <= dictionary[key][1]:
        print("Wynik to:", key)
        break

lista = [50, 60, 80, 100]
ocena = 2
for i in lista:
    if wynik <= i:
        print("Wynik to:", ocena)
        break
    ocena += 1
