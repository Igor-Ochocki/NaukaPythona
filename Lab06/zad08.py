# 8. Podaj ile dni upłyneło od 1.01.2000 roku do aktualnej daty
import datetime
from datetime import *

now = datetime.now()
actual_date = date(now.year, now.month, now.day)
previous_date = date(2000, 1, 1)
difference = actual_date - previous_date
print(difference)
