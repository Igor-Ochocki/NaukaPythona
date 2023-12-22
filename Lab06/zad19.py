# 19. Dana jest lista składająca się z liczb całkowitych:
dane = [7, 3, 3, 9, 18, 6, 5, 24, 24, 4, 4, 5, 3, 7, 3, 24]
# Należy wyeliminować powtarzające się wartości w danej liście i posortować malejąco.
# (program ma działać dla dowolnej listy składającej się z liczb całkowitych)
unique = []

for i in dane:
    if i in unique:
        continue
    unique.append(i)

print(sorted(unique, reverse=True))

unique_d = {}
processed = []
for i in dane:
    if i in unique_d:
        continue
    unique_d[i] = 0
    processed.append(i)

print(sorted(processed, reverse=True))
