print('-----------Sequencia Fibonacci---------')
nElementos = int(input('\nDigite a quantidade de elementos desejada: '))
termo1 = 0
termo2 = 1
ultTermo = 0
contador =  nElementos
print('~'*nElementos*7)
while contador > 0:
    print('{}'.format(ultTermo), end=' -> ')
    ultTermo = termo1 + termo2
    termo2 = termo1
    termo1 = ultTermo
    contador -= 1
print('FIM')
print('~'*nElementos*7)