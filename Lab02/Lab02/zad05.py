# app05
# wyświetl tabliczkę mnożenia (instrukcja for - 9 kolumn i 9 wierszy)


buf = ""
#[0,1,2,3,4,5,6,7,8]
for col in range(1,10):
    for row in range(1,10):
        buf += str(col * row) + "\t"
    print(buf)
    buf = ""


for col in range(1,10):
    for row in range(1,10):
        print(str(col * row) + "\t", end = "")
    print("") # printuje nową linię
