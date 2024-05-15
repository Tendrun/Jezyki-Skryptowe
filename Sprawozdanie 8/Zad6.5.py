import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

# Definiowanie pochodnej funkcji
def df(x):
    return 2*x

points = [-2, 0, 1]

x = np.linspace(-3,2, 400)
plt.plot(x, x**2, label='x^2', color='blue')

for i, color in zip(points, ['red', 'green', 'purple']):
    y = df(i)*(x - i) + f(i)
    plt.plot(x, y, label=f"Styczna w punkcie x={i}", color=color)

plt.title('Wykresy funkcji x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()