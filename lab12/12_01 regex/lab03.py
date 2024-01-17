# Sprawdź ile adresów email jest poprawnych i wyświetl w postaci listy, które są poprawne
import re

email = 'a1_f@wp.pl, a1_f@wp.pl, a3@wp.pl, stundet@p.pl, stundet@p..pl, student.p.lodz.pl.'

# wynik = re.findall(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.+[A-Z]{2,}', email, re.IGNORECASE)


wynik = re.findall(r'([A-Z0-9._-]+@([A-Z0-9]+\.)+[A-Z]{2,3})', email, re.IGNORECASE)
# wynik = re.match(r'^[A-Z0-9._+%-.]+@[A-Z0-9-]+\.+[A-Z]{2,}$', email, re.IGNORECASE)
emails = email.replace(" ", "").split(",")
for i in emails:
    wynik = re.fullmatch(r'[A-Z0-9._-]+@([A-Z0-9]+\.)+[A-Z]{2,3}', i, re.IGNORECASE)
    if wynik:
        print(wynik.group(0))
# if wynik:
#     print('ok')
#     for i in wynik:
#         print(i[0])
#     print(wynik.__len__())
# else:
#     print('No')
