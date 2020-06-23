p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
contador = 0
termo = p1
nTermos = 10
while contador <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += r
    contador += 1
print('FIM')


