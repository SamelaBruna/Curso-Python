aluno = {}
aluno['Nome']= input('Nome: ')
aluno['Media']= float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] >= 7.0:
    aluno['Situação'] = "Aprovado"
else:
    aluno['Situação'] = "Reprovado"

for k, v in aluno.items():
    print(f'{k} é igual a {v}')


#print('Nome é igual a', aluno['Nome'])
#print('Média é igual a', aluno['Media'])
#print('Situaçao é igual a', aluno['Situação'])