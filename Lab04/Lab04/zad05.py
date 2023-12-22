# 5. Losujemy liczby od 1-100 i po ilu losowaniach suma wyrzuconych wartości
#    tylko liczb parzystych będzie większa od wartości podanej jako parametr funkcji
#    count_random_even_numbers(sum_max).

from random import *

def count_random_even_numbers(sum_max):
    draws = 0
    sum = 0
    while sum < sum_max:
        a = randint(1, 100)
        if a % 2 == 0:
            sum += a
        draws += 1
    return draws

user_input = int(input("Podaj liczbę: "))

print(count_random_even_numbers(user_input))
