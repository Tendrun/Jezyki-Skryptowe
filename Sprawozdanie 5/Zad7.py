import re

inw = open("inw_plik.txt", mode="r", encoding="utf-8")

lines = inw.read()

words = re.split(" |\n", lines)


for i, word in enumerate(words):
    print(f"{word} {i}")
    nowy_plik = open(f"{word} {i}", "w.txt", encoding="utf-8")


print(words)