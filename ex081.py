lista = []
contador = 0
while True:
  num = int(input('Digite um número: '))
  lista.append(num)
  contador += 1
  opc = str(input('Deseja continuar? [S/N]: ')).upper()
  while opc != 'S' and opc != 'N':
    opc = str(input('Quer continuar? [S/N]: ')).upper()
  if opc == 'N':
    break

print('--'*20)
print(f'Foram digitados {contador} elementos')
lista.sort(reverse = True)
print('Lista ordenada em ordem decrescente {}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 NÃO faz parte da lista')