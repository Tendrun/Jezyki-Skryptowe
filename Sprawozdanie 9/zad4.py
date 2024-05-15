import struct
stalopozycyjnyWyk = bin(int(-245))
stalopozycyjnyMantysa = bin(25)
print(f"Liczba -245,25 w zapisie stałopozycyjnym {stalopozycyjnyWyk},{stalopozycyjnyMantysa}")

num = -245.25

binary_representation = bin(int.from_bytes(struct.pack('!f', num), 'big'))

print(f"Liczba -245,25 w zapisie zmiennopozycyjnym {binary_representation}")
