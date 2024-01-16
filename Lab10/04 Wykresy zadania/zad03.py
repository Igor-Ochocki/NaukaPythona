# Utwórz wykres 3D przedstawiający funkcję z = x**2 + y**2 dla zakresu
# x oraz y od -10 do 10. Dodaj siatkę, etykiety osi i tytuł wykresu.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10., 10., 100)
y = np.linspace(-10., 10., 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, cmap='viridis')

ax.set_xlabel("Oś x")
ax.set_ylabel("Oś y")
ax.set_zlabel("Oś z")
ax.grid()
ax.set_title("Wykres 3D funkcji z = x**2 + y ** 2")
plt.show()
