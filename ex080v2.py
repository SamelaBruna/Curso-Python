lista = []
#PROGRAMA APENAS PRA ORDENAR
for i in range(0,5):
    num = int(input('Digite o numero: '))
    lista.append(num)
print(lista)
for j in range(0,5):
    for i in range(j, 5):
        if lista[j] > lista[i]:
           nAux = lista[i]
           lista[i] = lista[j]
           lista[j] = nAux

print('Lista ordenada:',lista)