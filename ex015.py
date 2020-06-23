dias = int(input('Quantos dias de aluguel? '))
kmRod = float(input('Quantos km rodados? '))
total = (dias * 60) + kmRod * 0.15
print('O total a pagar é R${:.2f}'.format(total))