valCas = float(input('Digite o valor da casa R$: '))
sal =   float(input('Digite o seu salario R$: '))
anos = int(input('Em quantos anos deseja pagar? '))
valPrest = valCas / (anos*12)
print('O valor da prestação mensal ficou R${:.2f}'.format(valPrest))
if valPrest > ((30/100) * sal):
    print('Mas infelizmente seu empréstimo será NEGADO, excedeu 30% do salário')
else:
    print('Empréstimo APROVADO!')