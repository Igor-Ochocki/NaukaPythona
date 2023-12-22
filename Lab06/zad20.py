# 20. Mamy teskt:
dane = 'Litwo, Ojczyzno moja! ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko się dowie, kto cię stracił. Dziś piękność twą w całej ozdobie widzę i opisuję, bo tęsknię po tobie'
# Policz: - ile jest spacji w danym tekście.
#         - ile jest znaków pisanych dużymi literami
#         - ile jest znaków pisanych małymi literami.
#         - ile jest pozostałych znaków.
# Przekształć tekst na listę, gdzie separatorem elementu jest spacja.

spacje = 0
duze = 0
male = 0
pozostale = 0
# duze od 65 do 90
# male od 97 do 122
for i in dane:
    if i == " ":
        spacje += 1
        continue
    if i.isupper():
        duze += 1
        continue
    if i.islower():
        male += 1
        continue
    # if 65 <= ord(i) <= 90:
    #     duze += 1
    #     continue
    # if 97 < ord(i) <= 122:
    #     male += 1
    #     continue
    # if ord(i) > 127:
    #     if i.upper() == i:
    #         duze += 1
    #         continue
    #     if i.lower() == i:
    #         male += 1
    #         continue
    pozostale += 1

print(f"Spacje: {spacje}\nMale: {male}\nDuze: {duze}\nInne: {pozostale}")
