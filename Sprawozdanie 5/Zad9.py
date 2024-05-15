inw = open("inw_plik.txt", mode="r", encoding="utf-8")

lines = inw.read()

count = 1
result = ""

for i in lines:
    if i == 'w':
       result += "{w" + format(count, '#06x') + "}"
       count += 1
    else:
        result += i


print(result)