salario = float(input('Qual o preço do produto?R$ '))
reajuste = salario + (salario * (15/100))
print('O salário que custava R${}, com 15% de aumento, passa a ser R${:.2f}'.format(salario,reajuste))