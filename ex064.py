num = 0
tot = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    tot += 1
    soma += num
print('Você digitou {} números e a soma entre eles foi {}'.format(tot-1,soma-999))