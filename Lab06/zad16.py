# 16. Do bieżącej daty dodaj 3 tygodnie lub 21 dni (datetime.timedelta(...))

from datetime import *

teraz = datetime.now()
print(teraz + timedelta(days=21))
print(teraz + timedelta(weeks=4, days= 1))
