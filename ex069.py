cont18 = 0
contHom = 0
contMul20 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]: ')).upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).upper()
    #print('Quer continuar?')
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        contHom += 1
    if sexo == 'F' and idade < 20:
        contMul20 += 1
    print('-' * 20)
    opc =str(input('Quer continuar?')).upper()

    while opc != 'N' and opc != 'S':
        opc = str(input('Quer continuar? [S/N]')).upper()
    if opc == 'N':
        break
print('=======FIM DO PROGRAMA=======')
print('Pessoas acima de 18 anos: {}\nHomens cadastrados: {}\nMulheres com menos de 20 anos: {}'.format(cont18,contHom,contMul20))