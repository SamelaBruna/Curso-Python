sum = 0
qntVal = 0
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0:
        sum += c
        qntVal +=  1
        #print(c,end= ' ')
print('\nA soma de todos os {} valores solicitados é {}:'.format(qntVal,sum))