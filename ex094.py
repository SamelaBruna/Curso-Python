pessoa = {}
lista = []
somIdade = 0
while True:
    pessoa['Nome'] = input('Nome: ').title()
    pessoa['Sexo'] = input('Sexo [F/M] ').upper()
    pessoa['Idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    somIdade += pessoa['Idade']
    opc = input('Deseja continuar? [S/N] ')
    if opc in 'Nn':
        break
print('-=' * 30)
print(lista)
print('-=' * 30)
print(f'- O grupo tem {len(lista)} pessoas')
print(f'- A média da idade é {somIdade / len(lista):.2f} anos')
print(f'- As mulheres cadastradas foram: ', end='')

for i in range(0, len(lista)):
    if lista[i]['Sexo'] == 'F':
        print(lista[i]["Nome"], end=' ')
print()
print('- Lista das pessoas que estão acima da média: ')
for i in range(0, len(lista)):
    if lista[i]['Idade'] > (somIdade / len(lista)):
        for k, v in lista[i].items():
            print(f'{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
