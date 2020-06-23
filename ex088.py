from random import randint
lista = []
jogos = []
print('--'*20)
print('              Mega Sena')
print('--'*20)
quantidade = int(input('Quantos jogos você quer fazer? '))
contJogos = 0
contNum = 0
print(f'\n       Sorteando {quantidade} jogos\n')
while contJogos < quantidade:
    contNum = 0
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            contNum +=1
        if contNum >= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    contJogos += 1
for i in range(0,len(lista)):
    print(f'Jogo {i+1}:',lista[i])
print('--'*20)
print('           BOA SORTE')



