lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if (num in lista) == False:
        lista.append(num)
        print('Valor adicionado com sucesso')
    opc = str(input('Quer continuar? [S/N]: ')).upper()

    while opc != 'S' and opc != 'N':
        opc = str(input('Quer continuar? [S/N]: ')).upper()
    if opc == 'N':
        break

print('Você digitou os valores:',sorted(lista))