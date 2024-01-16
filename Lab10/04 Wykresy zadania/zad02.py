# Utwórz dwa osobne wykresy dla funkcji y = sin(x) i y = cos(x)
# (najpierw wyświetlana jest pierwsza funkcja a po jej zamknięciu druga)
# dla x zawierającego 4*pi (2 okresy)

import matplotlib.pyplot as plt
import numpy as np
import math

def second_plot(event):
    plt.plot(x, f2, label="y = cos(x)", color='b')
    plt.show()

x = np.linspace(0., math.pi * 4, 1000)
print(x)
f1 = np.sin(x)
f2 = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_surface(x, f1, label="y = sin(x)", color='b')
ax.set_xlabel("Oś x")
ax.set_ylabel("Oś y")
plt.show()