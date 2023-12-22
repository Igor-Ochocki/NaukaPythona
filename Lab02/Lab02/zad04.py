#app04
#Mamy przykładową zmienną data: data = ['jeden','dwa','trzy','cztery','pięć','sześć']
data = ['jeden','dwa','trzy','cztery','pięć','sześć']
#Wyświetl w kolejnych linijkach kolejną pozycję w postaci ciągu znaków np.
#jeden
#  j
#  e
#  d
#  e
#  n
# ...

# string -> ciąg znaków // python - string -> array(char) -> string[0] --> element 0 stringa

for word in data: # === for i in range(len(data)): x = data[i]
    print(word)
    for letter in word:
        print(letter)
    print("-------")