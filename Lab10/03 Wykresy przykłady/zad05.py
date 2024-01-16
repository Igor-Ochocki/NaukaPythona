# Utwórz wykres kołowy przedstawiający procentowy udział trzech kategorii w całkowitej sprzedaży. Dodaj etykiety.

import matplotlib.pyplot as plt

labels = ['Kategoria A', 'Kategoria B', 'Kategoria C']
sizes = [30, 45, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=0, colors=['r', 'g', 'b'])

plt.axis('off')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Wykres kołowy')
plt.show()
