matriz= [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
soma3coluna=0
maior = 0
for linha in range (0,3): #inserir valores na matriz
    for coluna in range (0,3):
       matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

for linha in range (0,3): #imprimir a matriz
    for coluna in range (0,3):
        print([matriz[linha][coluna]], end = ' ')
        if matriz[linha][coluna] % 2 == 0: #verificar e somar os pares
            soma += matriz[linha][coluna]
    print()

for linha in range (0,3): #somar apenas a 3° coluna
    soma3coluna += matriz[linha][2]
for coluna in range (0,3): #percorrer a 2° linha toda e verificar o maior
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(soma,soma3coluna, maior)
