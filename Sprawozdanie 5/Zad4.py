inw = open('inw_plik.txt', mode='r' ,encoding='utf-8')

#z malych liter
def Punkt1():
    lines = []
    for line in inw:
        lines.append(line.lower())


    return lines







# z duzych liter
def Punkt2():
    lines = []
    for line in inw:
        lines.append(line.lower())

    return lines










#Kazdy wers z duzej litery
def Punkt3():
    lines = inw.readlines()
    lines = [line.capitalize() for line in lines]
    for line in lines:
        print(line)














#Co drugi z duzej, co drugi z malej
def Punkt4():
    lines = inw.readlines()
    for i in range(len(lines)):
        if i % 2 == 0:
            print(lines[i].upper())
        else:
            print(lines[i].lower())









#Co druga litera z duzej, co druga litera z malej
def Punkt5():
    lines = inw.read()
    for i in range(len(lines)):
        if i % 2 == 0:
            print(lines[i].upper())
        else:
            print(lines[i].lower())








#Co druga litera z duzej, co druga litera z malej
def Punkt6():
    lines = inw.read()
    for i in range(len(lines)):
        if i % 2 == 1:
            print(lines[i])







def Punkt7():
    lines = inw.read()
    for i in range(len(lines) - 1, -1, -1):
        print(lines[i])



