# Dodatkowe (niewymagane)
# 1. Podaj wartość funkcji w punkcie x  dowolnej funkcji
#    np. f(x) = 2*x*x + 7*x + 6 + 1/x.
#    Całą funkcję podajemy z klawiatury (korzytsamy z funkcji eval). Punkt x także podajemy z klawiatury.

x = int(input("Podaj punkt x : "))
user_input = input("Podaj funkcję: ")
if "=" in user_input:
    fn = eval(user_input[user_input.index("=")+2::])
else:
    fn = eval(user_input)
print(fn)