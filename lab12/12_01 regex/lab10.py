# Wyszukiwanie i wyświetlanie adresów IP w tekście:
# Znajdź wszystkie adresy IP w danym tekście
text = "Adresy IP serwerów to 168.1.1, 10.0.0.1, oraz 172.16.0.1"
import re

regex = re.compile(r"(\d|[1-9]\d|[1-9]\d{2})[.](\d|[1-9]\d|[1-9]\d{2})[.](\d|[1-9]\d|[1-9]\d{2})[.](\d|[1-9]\d|[1-9]\d{2})")

wynik = regex.finditer(text, re.MULTILINE)

for matchIdx, match in enumerate(wynik, start=1):
   print(f"Element {matchIdx} o wartości {match.group()} jest adresem ip")