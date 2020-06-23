jogador = {}
listaJogadores = []
sumGols = 0
listaGols = []
'------------------------- FALTA TERMINAR---------------------------'
while True:
    sumGols = 0
    jogador['Nome'] = input('Nome: ')
    numPar = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for i in range (0,numPar) :
        numGol = int(input(f'Quantos gols na partida {i +1 }? '))
        listaGols.append(numGol)
        sumGols += numGol

    jogador['Gols'] = listaGols[:]
    jogador['Total'] = sumGols
    listaJogadores.append(jogador.copy())
    listaGols.clear()

    opc = input('Deseja Continuar? [S/N] ')

    print('--'*30)
    if opc in 'Nn':
        break
print(listaJogadores)
print('-='*30)
print(f'{"cod":<10}  {"nome":<8}  {"gols":<5} {"Total":>10}')
for i in range (0,len(listaJogadores)):
   print(f'{i:<10} {listaJogadores[i]["Nome"]:<8} {str(listaJogadores[i]["Gols"]):<5} {listaJogadores[i]["Total"]:>10}')

while True:
    opc2 = int(input('Mostrar dados de qual jogados?'))

    if opc2 == 999:
        break
    if opc2 >= len(listaJogadores):
        print('Erro! Não existe esse jogador')
    else:
        print(f'-- LEVANTAMENTO DO JOGAGOR {listaJogadores[opc2]["Nome"]}')
        for i, g in enumerate(listaJogadores[opc2]['Gols']):
            print(f'  No jogo {i+1} fez {g} gols')
    print('--'*20)
print('<< Volte Sempre')