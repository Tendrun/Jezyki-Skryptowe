inw = open('inw_plik.txt', mode='r' ,encoding='utf-8')

lista = [x.replace('\n', '') for x in inw.readlines()]

polczona_lista ="-".join(lista)

for line in polczona_lista:
    print(line)