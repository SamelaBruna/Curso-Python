sal = float(input('Digite o salário: '))
if sal > 1250.00:
    aumento = (sal * (10/100))
    print('O aumento será de R${:.2f};'.format(aumento))
    print('Logo seu novo salário ficará R${:.2f}'.format(sal + aumento))
else:
    aumento = (sal * (15/100))
    print('O aumento será de R${};'.format(aumento))
    print('Logo seu novo salário ficará R${:.2f}'.format(sal + aumento))