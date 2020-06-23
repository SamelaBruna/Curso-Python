from random import randint
contador = 0
print('VAMOS JOGAR PAR OU IMPAR')
print('-'*20)
while True:
    n1 = int(input('Digite um numero: '))
    nPc = randint(0,10)
    opc = str(input("Par ou Impar? [P/I] ")).upper()
    print('-'*20)
    soma = n1 + nPc
    if soma % 2 == 0:
        cond = 'PAR'
    else:
        cond = 'IMPAR'
    print('Você jogou {} e o computador {}. Total de {} deu {}'.format(n1,nPc,soma,cond))
    print('-'*20)
    if opc == 'P' and soma % 2 == 0 or opc == 'I' and soma % 2 != 0 :
        print('Você venceu!\nVamos jogar novamente...')
        contador += 1
        print('-'*20)
    else:
        print('Você perdeu!')
        break
print(f'GAME OVER! Você venceu {contador} vezes')



