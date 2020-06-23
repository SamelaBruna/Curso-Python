#Cédulas de 50,20,10 e 1
from math import ceil, floor
ced50 = ced20 = ced10 = ced1 = 0
valor = int(input('Que valor você quer sacar? R$'))
valorNew = valor
while True:
    if valorNew >= 50:
        while floor(valorNew/50) > 0:
            ced50 += 1
            valorNew = valor - 50*(ced50)
            #print('ced50: ',ced50)

    elif valorNew < 50 and valorNew >= 20:
        while floor((valorNew/20)) > 0:
                #print(valorNew)
                ced20 += 1
                valorNew = valorNew - 20
                #print('ced20:',ced20)
    elif valorNew < 20 and valorNew >= 10:
        while floor((valorNew / 10)) > 0:
           # print(valorNew)
            ced10 += 1
            valorNew = valorNew - 10
    elif valorNew < 10 and valorNew >= 1:
        while floor((valorNew / 1)) > 0:
            #print(valorNew)
            ced1 += 1
            valorNew = valorNew - 1
    if valorNew == 0:
        #print('Ultimo valor: ',valorNew)
        break
print('ced50: {}\nced20: {}\nced10: {}\nced1: {}'.format(ced50,ced20,ced10,ced1))

#FAZER DE OUTRA MANEIRA!