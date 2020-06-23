from random import  randint

numRand = randint(0,5)
print('Vamos Jogar!?\nAcabei de pensar em um número entre 0 e 5, será que você consegue adivinhar?')
num = int(input('\nEm qual número pensei? '))
if num == numRand:
    print('Parabéns, você venceu! ')
else:
    print('Que pena, você perdeu! ')
