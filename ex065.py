opc = 'S'
contNum = 0
som = 0
menor = maior = 0
while opc == 'S' or opc == 's':
    num = int(input('Digite um número: '))
    som = som + num
    contNum += 1
    if contNum == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if num < menor:
            menor = num
    opc = str(input('Deseja continuar? '))

media = som/ contNum
print('Você digitou {} números\nA media entre eles foi {:.2f}, o maior número foi {} e o menor número foi {}'.format(contNum,media, maior, menor))
