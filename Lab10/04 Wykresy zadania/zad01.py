# Utwórz trzy funkcje na jednym wykresie y = x, y = 0.5*x**2, y = sqrt(x**4)
# x = np.arange(-5., 5., 0.1)
# Osie x i y mają być proporcjonalne, wyświetl siatkę.

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-5., 5., 0.1)
f1 = x
f2 = 0.5*x**2
f3 = np.sqrt(x**4)

plt.plot(x, f1, label='y = x', color='r')
plt.plot(x, f2, label='y = 0.5*x**2', color='g')
plt.plot(x, f3, label='y = sqrt(x**4)', color='b')
plt.grid()
plt.xlabel("Oś x")
plt.ylabel("Oś y")
plt.title("Wykresy funkcji")
plt.legend()
plt.show()