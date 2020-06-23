from random import randint
from time import sleep
print('{:=^40}'.format('JOKENPÔ'))
lista = ['Pedra', 'Papel', 'Tesoura']
jogador = int(input("""Escolha:
[0] - Pedra
[1] - Papel
[2] - Tesoura
Qual a sua jogada? """))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!!!')
computador = randint(0,2)

if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada Invalida')
else:
    print('-=' * 20)
    print('Computador: {}'.format(lista[computador]))
    print('Jogador: {}'.format(lista[jogador]))
    print('-=' * 20)
    if computador == 0:
        if jogador == 0:
            print("EMPATE!")
        elif jogador == 1:
            print("JOGADOR VENCEU!")
        elif jogador == 2:
            print("COMPUTADOR VENCEU!")

    elif computador == 1:
        if jogador == 0:
            print("COMPUTADOR VENCEU!")
        elif jogador == 1:
            print("EMPATE!")
        elif jogador == 2:
            print("JOGADOR VENCEU!")

    elif computador == 2:
        if jogador == 0:
            print("JOGAR VENCEU!")
        elif jogador == 1:
            print("COMPUTADOR VENCEU!")
        elif jogador == 2:
            print("EMPATE!")

