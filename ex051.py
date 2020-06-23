prim = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
a10 = prim + (10 - 1)*raz
for c in range (prim, a10, raz):
    print('{}'.format(c), end = ' -> ')
print('FIM')
