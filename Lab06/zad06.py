# 6. Podaj, w jaki dzień tygodnia urodził się Adam Małysz.
# Data podana może być dowolna. Zdefiniuj funkcję.
#  3 grudnia 1977
import datetime
from datetime import time
import locale

# locale.setlocale(locale.LC_TIME, "pl_PL") - polski język


def dzien_tyg(year, month, day):
    x = datetime.date(year, month, day)
    print(x.strftime('%A'))


dzien_tyg(1977, 12, 3)
