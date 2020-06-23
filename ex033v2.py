n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))
lista = [n1,n2,n3]
listaOrden = sorted(lista)
print('O maior número é {}'.format(listaOrden[2]))
print('O menor número é {}'.format(listaOrden[0]))