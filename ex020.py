from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
listaAlu = [a1,a2,a3,a4]
shuffle(listaAlu)
print('A ordem de apresentação é: {}'.format(listaAlu))