lista = []
listaPar = []
listaImpar = []

while True:
  num = int(input('Digite um número: '))
  lista.append(num)
  opc = str(input('Deseja continuar? [S/N]: ')).upper()
  if num % 2 == 0:
      listaPar.append(num)
  else:
      listaImpar.append(num)

  while opc != 'S' and opc != 'N':
    opc = str(input('Quer continuar? [S/N]: ')).upper()
  if opc == 'N':
    break


print('Lista {}\nLista de Pares {}\nLista de Impares {}'.format(lista,listaPar,listaImpar))