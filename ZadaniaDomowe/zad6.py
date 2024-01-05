# Napisz funkcję bubble_sort która przyjmuje listę liczb całkowitych i zwraca posortowaną listę tych liczb
# wykorzystaj Sortowanie Bąbelkowe

# bonus : wczytaj dane (z inputu)

tabela = []

a = int(input("Podaj ilość elementów w tablicy: "))

for i in range(0, a):
    b = int(input("Podaj elementy tablicy: "))
    tabela.append(b)

print(f"Nieposortowana tablica: {tabela}")
licznik = 0
def bubble_sort(tabela):
    for i in range(0, len(tabela)):
        for j in range(0, len(tabela) - 1):
            if(tabela[j] > tabela[j + 1]):
                # zm = tabela[j]
                # tabela[j] = tabela[j + 1]
                # tabela[j + 1] = zm
                tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
    return tabela

tabela = bubble_sort(tabela)
print(f"Posortowana tabela: {tabela}")
print(f"Zajelo to {licznik} operacji")