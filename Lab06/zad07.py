# 7. Ile aktualnie lat ma Adam Małysz (albo dowolna osoba).
# Zdefiniuj funkcję how_old(date).
import math
from datetime import *


def how_old(birthday):
    now = datetime.now()
    difference = now - birthday
    return math.floor(difference.days / 365)


print(how_old(datetime(1977, 12, 3)))
