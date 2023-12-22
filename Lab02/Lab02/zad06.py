# app06
# - Wyświetlamy liczby od 10 do 0 w jednej linijce a przy liczbie 3 wychodzimy z pętli (konstrukcja while oraz instrukcją break)
i = 10
while i >= 0:
    print(str(i) + " ", end="")
    if i == 3:
        break # przechodzi do linii 8
    i -= 1

# - Wykonujemy to samo co wyżej tylko konstrukcja while ma na stałe postać - while True: (zawsze prawda)
print("") # - nowa linia
i = 10
while True:
    print(str(i) + " ", end="")
    if i == 3:
        break  # przechodzi do linii 8
    i -= 1

# - Wyświetlamy liczby od 100 do 90 w jednej linijce a przy liczbie 95 i 93 pomijamy wyświetlanie (konstrukcja while oraz instrukcją continue (bez break))
print("") # - nowa linia
# - Python (and | or) C/C++ (&& | ||)
i = 100
while i >= 90:
    if i == 95 or i == 93:
        i -= 1
        continue # przechodzi do linii 23
    print(str(i) + " ", end="")
    i -= 1


# - Wykonujemy to samo co wyżej tylko konstrukcja while ma na stałe postać - while True: (zawsze prawda) (z instrukcją continue i break)
print("") # - nowa linia
# - Python (and | or) C/C++ (&& | ||)
i = 100
while True:
    if i == 95 or i == 93:
        i -= 1
        continue # przechodzi do linii 23
    print(str(i) + " ", end="")
    i -= 1
    if i < 90:
        break


