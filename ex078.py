lista = []
posMax = []
posMin = []
for i in range (0,5):
    lista.append(int(input(f'Digite um valor para a posição {i}: ')))

for posicao, valores in enumerate(lista):
    if valores == max(lista):
       posMax.append(posicao)
    if valores == min(lista):
        posMin.append(posicao)

print(max(lista),posMax)
print(min(lista),posMin)






