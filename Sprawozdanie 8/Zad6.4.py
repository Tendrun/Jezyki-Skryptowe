import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

"""
plt.plot(x, np.sin(x), label='cos(x)', color='blue')
for phi, color in zip([1/4, 1/3, 1/2], ['red', 'green', 'purple']):
    plt.plot(x, np.sin(x + phi), label=f'sin(x + {phi})', color=color)
"""

plt.plot(x, np.cos(x), label='cos(x)', color='black', linestyle='--')
for phi, color in zip([1/4, 1/3, 1/2], ['red', 'green', 'purple']):
    plt.plot(x, np.cos(x + phi), label=f'cos(x + {phi})', color=color)

plt.title('Wykresy funkcji cos(x + φ)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()