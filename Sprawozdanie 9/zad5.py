def dectobin(n):
    if n == 0:
        return "0"
    bin_str = ""
    while n > 0:
        bin_str = str(n % 2) + bin_str
        n //= 2
    return bin_str

print("0 =", dectobin(0))
print("26 =", dectobin(26))
print("15 =", dectobin(15))
print("13 =", dectobin(13))

