# 6. Tabliczka mnożenia od 1..10 z tym, że liczby wyrównujemy w kolumnach do prawej strony (liczymy do 100)

for i in range(1,11):
    for j in range(1, 11):
        text = str(i*j) + " "
        print(f"{text : >4}", end="")
    print("")