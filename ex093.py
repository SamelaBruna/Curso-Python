jogador = {}
listaGols = []
sumGols = 0

jogador['Nome'] = input('Nome: ')
numPar = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for i in range (0,numPar) :
    numGol = int(input(f'Quantos gols na partida {i}? '))
    listaGols.append(numGol)
    sumGols += numGol

jogador['Gols'] = listaGols
jogador['Total'] = sumGols

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {numPar} partidas.')
for i in range(0,numPar):
    print(f'   => Na partida {i}, fez {listaGols[i]} gols')
print(f'Foi um total de {sumGols}')