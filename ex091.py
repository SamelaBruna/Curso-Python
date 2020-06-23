from random import randint
from time import  sleep
from operator import itemgetter
jogo = {'J1': randint(1,6), 'J2': randint(1,6), 'J3': randint(1,6), 'J4':randint(1,6)}
ranking = {}
for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = sorted(jogo.items(), key = itemgetter(1), reverse= True) #me retorna uma lista
print('--'*20)
print('== RANKING DOS JOGADORES ==')

for i in range(0,len(ranking)):
    print(f'{i+1:>2} lugar: {ranking[i][0]} com {ranking[i][1]} ')
