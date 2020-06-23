from math import sqrt
catOp = float(input('Valor do cateto oposto: '))
catAd = float(input('Valor do cateto adjacente: '))
hipo = sqrt(catOp*catOp + catAd*catAd)
print('O valor da hipotenusa é: {:.2f} '.format(hipo))
