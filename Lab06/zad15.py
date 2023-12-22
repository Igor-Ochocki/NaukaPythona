# 15. Wyświetl kalendarz za rok 2022 i zobacz czy układ Świąt Bożego Narodzenia wygląda atrakcyjnie, czy nie
# (jeżeli święta są w tygodniu to OK, jeśli zahaczają o sobotę i niedzielę to Nie)
import calendar
from datetime import *


cal = calendar.Calendar(0).yeardatescalendar(2022)
for quarter in cal:
    for month in quarter:
        # struktura miesiąca i tygodnii
        for week in month:
            for day in week:
                if day.year != 2022:
                    continue
                print(f"{day.strftime('%Y-%m-%d %a')}")
