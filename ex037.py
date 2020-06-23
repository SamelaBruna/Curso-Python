num = int(input('Digite o número desejado: '))
escolha = int(input("""Deseja converter pra qual base? 
[1] - Binário
[2] - Octal
[3] - Hexadecimal \n"""))

if escolha == 1:
    print('O numero {} em binário é: {}'.format(num,bin(num)))
elif escolha == 2:
    print('O numero {} em octal é: {}'.format(num,oct(num)))
elif escolha == 3:
    print('O numero {} em hexadecimal é: {}'.format(num,oct(num)))
