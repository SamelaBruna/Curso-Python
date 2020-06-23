conjNum = [[], []]
for i in range (0,7):
    num = int(input(f'Digite o {i+1} valor: '))
    if num % 2 == 0:
        conjNum[0].append(num)

    else:
        conjNum[1].append(num)
print(conjNum)
conjNum[0].sort()
conjNum[1].sort()
print('Os valores pares digitados foram: ',conjNum[0])
print('Os valores impares digitados foram: ', conjNum[1])


'''for j in range(0,len(conjNum[0])):
    for i in range(j, len(conjNum[0])):
        if conjNum[0][j] > conjNum[0][i]:
           nAux = conjNum[0][i]
           conjNum[0][i] = conjNum[0][j]
           conjNum[0][j] = nAux

for j in range(0,len(conjNum[1])):
    for i in range(j, len(conjNum[1])):
        if conjNum[1][j] > conjNum[1][i]:
           nAux = conjNum[1][i]
           conjNum[1][i] = conjNum[1][j]
           conjNum[1][j] = nAux'''
#funciona o comentario de cima mas utilizando o sort

