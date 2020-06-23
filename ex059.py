n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opc = 0
while opc != '5':
    print(''' ------------------------------
    [1] - Somar 
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do programa''')
    opc = str(input('Qual é a sua opção? '))
    if opc == '1':
        print('A soma entre {} + {} = {}'.format(n1,n2,n1+n2))
    elif opc == '2':
        print('A multiplicação entre {} * {} = {}'.format(n1, n2, n1 * n2))
    elif opc == '3':
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é {}'.format(n1,n2,maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
        else:
            print('Não existe maior, ambos são iguais')
    elif opc == '4':
        print('Informe os números novamente')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif opc == '5':
        print('Finalizando...')
    else:
        opc = str(input('Dados inválivos, digite novamente: '))
print('Fim do programa!')



