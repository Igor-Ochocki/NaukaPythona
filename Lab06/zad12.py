# 12. Wykorzystaj funkcję sorted do sortowania listy z wyrazami
#  względem długości stringu.

lista = ["sdj", " jasdfhja", "jhsdafsj", "kjhadfshjgasdhjkdfashjkasdffasd",  "ljsdajkass", "ljasdfhgjasuisdsd", "asdj"]
print(sorted(lista, key=len, reverse=True))
