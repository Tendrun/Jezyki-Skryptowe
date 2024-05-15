import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad


# Definiowanie modelu
def model(x, a, b, c):
    return a * np.log(x + b) + c

# Dane wejściowe
x = np.array([0.1, 0.4, 0.7, 1.0, 1.3, 1.6, 1.92, 2.22, 2.53, 2.83, 3.14, 3.44,
3.74, 4.05, 4.35, 4.66, 4.96, 5.26, 5.57, 5.87, 6.18, 6.48, 6.78, 7.09, 7.39,
7.7, 8.0, 8.3, 8.61, 8.91, 9.22, 9.52, 9.83, 10.13, 10.43, 10.74, 11.04, 11.35,
11.65, 11.95, 12.26, 12.56, 12.87, 13.17, 13.47, 13.78, 14.08, 14.39, 14.69, 15])

y = np.array([0.09, 0.57, 0.97, 1.29, 1.57, 1.82, 2.04, 2.24, 2.42, 2.58, 2.74,
2.88, 3.01, 3.13, 3.25, 3.36, 3.47, 3.57, 3.66, 3.75, 3.84, 3.92, 4.00, 4.08,
4.15, 4.22, 4.29, 4.36, 4.42, 4.48, 4.54, 4.60, 4.66, 4.72, 4.77, 4.82, 4.87,
4.92, 4.97, 5.02, 5.06, 5.11, 5.15, 5.20, 5.24, 5.28, 5.32, 5.36, 5.40, 5.44])

# Dopasowanie modelu do danych
popt, pcov = curve_fit(model, x, y)

# Wydrukowanie wyników
print("a = %s , b = %s, c = %s" % (popt[0], popt[1], popt[2]))

x_model = np.linspace(min(x),max(x), 1000)
y_model = model(x_model, *popt)

# Obliczenie całki oznaczonej
integral, error = quad(model, 1, 3, args=tuple(popt))

print(f"Całka oznaczona modelu z zakresu (1, 3) wynosi: {integral}")

# Generowanie punktów dla wykresu obszaru pod krzywą
x_fill = np.linspace(1, 3, 100)
y_fill = model(x_fill, *popt)

plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Dane')
plt.plot(x_model, y_model, color='red', label='Model: y = a log(x + b) + c')
plt.fill_between(x_fill, y_fill, color='gray', alpha=0.5, label=f'Całka: {integral:.2f}')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres punktów danych, modelu logarytmicznego i całki oznaczonej')
plt.grid(True)
plt.show()