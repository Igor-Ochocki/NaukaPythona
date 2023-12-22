# 7. Tabliczka mnożenia z wykorzystaniem instrukcji while i ewentualnie if (liczymy do 100) - efekt jak w zdaniu zad06.py
i = 1
while i < 11:
    j = 1
    while j < 11:
        text = str(i*j) + " "
        print(f"{text : >4}", end="")
        j += 1
    i += 1
    print("")
