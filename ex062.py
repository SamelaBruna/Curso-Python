#-------resol do guanabara------
p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
contador = 0
termo = p1
nTermos = 10
while nTermos > 0:
    print('{}'.format(termo), end=' -> ')
    termo += r
    nTermos -= 1
    if nTermos == 0:
        print('PAUSA')
        nTermos = int(input('\nQuantos termos voce quer mostrar a mais? '))