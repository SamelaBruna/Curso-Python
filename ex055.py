listaPeso = []
for i in range (0,5):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i+1)))
    listaPeso.append(peso)
maiorPeso = max(listaPeso)
menorPeso = min(listaPeso)
print(maiorPeso, menorPeso)