lista = []
dados = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    idade = float(input('Peso: '))
    dados.append(nome)
    dados.append(idade)
    #dados.append([input('nome'), float(input('peso: '))])
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    opc = str(input('Quer continuar? [S/N]: '))
    if opc in 'Nn':
        break
print(f'Ao todo vc cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')

for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end = '')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:

        print(p[0], end= '')
