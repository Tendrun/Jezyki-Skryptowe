# Prawdziwa wartość
x = 0.2

# Aproksymowana wartość
x0 = 0.1875

# Obliczanie błędu bezwzględnego
bladBezwgledny = abs(x - x0)

# Obliczanie błędu względnego
bladWzgledny = bladBezwgledny / x

# Wydrukowanie wyników
print(f"Błąd bezwzględny: {bladBezwgledny}")
print(f"Błąd względny: {bladWzgledny}")