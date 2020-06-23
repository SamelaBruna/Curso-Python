from datetime import date

data_atual = date.today()

pessoa = {}
pessoa['Nome'] = input('Nome: ')
data = int(input('Ano de Nascimento:'))
pessoa['Idade'] = data_atual.year - data
pessoa['CNTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CNTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] =  pessoa['Idade'] + ((pessoa['Contratação'] + 35) - data_atual.year)
print()
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')