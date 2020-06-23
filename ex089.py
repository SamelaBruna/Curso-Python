lista = []
aluno = []
media = 0
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: ' ))
    n2 = float(input('Nota 2: '))
    opc = input('Deseja continuar? [S/N]: ')
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    lista.append(aluno[:])
    aluno.clear()
    if opc in 'Nn':
        break
print(f'{"No.":<4} {"Nome":<10} {"Média":>12}')
print('--'*20)
for al in range(0,len(lista)):
    media = (lista[al][1] + lista[al][2])/2
    print(f'{al:<4} {lista[al][0]:<10}',end = '')
    print(f'{media: >12}', end = ' ')
    print()
print('--'*20)

while True:
    opcAl = int(input('Mostrar notas de qual alunos?'))
    if opcAl == 999:
        print('Finalizando')
        break
    if opcAl <= len(lista) -1:
        print(f'As notas de {lista[opcAl][0]} são {lista[opcAl][1:]}')
        print('--'*20)

