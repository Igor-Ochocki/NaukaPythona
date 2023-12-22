# 5. Wykorzystaj moduł datetime do podania w jednej linijce
#   rok-miesiąc-dzień oraz godzina:minuty:sekundy
#   w danym momencie z wykorzystaniem najnowszego formatowania danych f-string (f').
from datetime import *

date = datetime.now()
print(f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}")
print(f"{date.strftime('%Y-%m-%d %H:%M:%S')}")
