n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2 )/2
print('Sua média é', media)
if media < 5.0:
    print('REPROVADO')
elif 5.0 <= media <=6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')