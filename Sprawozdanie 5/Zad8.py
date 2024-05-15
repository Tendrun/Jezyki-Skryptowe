inw = open("inw_plik.txt", mode="r", encoding="utf-8")

lines = inw.read()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = lines.replace("a","{}")

for i, letter in enumerate(alphabet):
    words = words.format(letter, *['{}'] * words.count('{}'))

print(words)