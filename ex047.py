numPar = 0
for c in range(1,51):
    if c % 2 == 0:
        numPar += 1
        print(c,end= ' ')
print('\nTotal de pares:',numPar)