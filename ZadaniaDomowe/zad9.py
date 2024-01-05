# napisz funkcję generującą hasło o podanej ilości znaków


# bonus : funkcja ma generować tylko silne hasło ( o ile jest to możliwe)
# silne hasło posiada przynajmniej 8 znaków, przynajmniej 1 mała i 1 dużą literę, przynajmniej jedną cyfrę a także znak
# specjalny

import random
import string

def strong_password(dlugosc):
        haslo = ''.join(random.choice(string.ascii_letters + string.punctuation + string.digits) for i in range(dlugosc))
        print(haslo)

strong_password(8)
