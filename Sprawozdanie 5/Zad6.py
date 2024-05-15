inw = open("inw_plik.txt", mode="r", encoding="utf-8")

lines = inw.read()
new_lines = []


new_lines.append(lines.replace(" ", ""))

for line in new_lines:
    print(line)