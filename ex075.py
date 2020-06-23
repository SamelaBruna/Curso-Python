tupla = (int(input('Digite um numero: ')),int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
 print('Você digitou os valores: ',tupla)
print('O valor 9 apareceu {} vezes'.format(tupla.count(9)))
if 3 in tupla:
    print('O valor 3 apareceu na {}° posição'.format(tupla.index(3)+1))
else:
    print('Você não digitou 3')
print('Os valores pares digitados foram: ')
for num in tupla:
    if num % 2 == 0:
        print(num, end = ' ')
