def binToDec(number = ''):
    s = 0
    m = 0
    m_index = 0
    c = 0
    for i in range(0, len(number)):
        #znak
        if i == 0:
            if number[i] == '1':
                s = -1
                #ujemne
            elif number[i] == '0':
                s = 1
                #dodatnie
        #cecha
        elif 2 <= i <= 3:
            num = int(number[i]) * 2**int(number[i])
            c += num
        #mantysa
        elif 4 <= i <= 7:
            m_index += 1
            num = int(number[i]) * 2**-m_index
            m += num

    decNumber = s * 2**c * m
    return decNumber

A = '10101101'
B = '11101010'
C = '01001000'
D = '01111011'
E = '01000111'

print("A = ", binToDec(A))
#print("B = ", binToDec(B))
#print("C = ", binToDec(C))
#print("D = ", binToDec(D))
#print("E = ", binToDec(E))