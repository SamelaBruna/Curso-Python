#-------Senti Dificuldade------#
maioresIdadeM = 0
somIdade = 0
menor20 = 0
for i in range (0,4):
    print('-----{}° PESSOA{}'.format(i+1,'-----'))
    nome = str(input('Nome: ').title()).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somIdade += idade
    if i == 0 and sexo == 'M':
        maioresIdadeM = idade
        nomeOld = nome
    if sexo == 'F' and idade <= 20:
        menor20 += 1
    if sexo == 'M' and idade > maioresIdadeM:
        maioresIdadeM = idade
        nomeOld = nome


mediaIdade = somIdade / 4
print('\nA media de idade do grupo é de {:.1f} anos'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioresIdadeM, nomeOld))
#como as listas sao todas de tamanho 4, pega a posiçao que se encontra o maior idade da lista de idades e esse sera o mesmo indice da lista de nomes
print('A todo existe {} mulher(es) com menos de 20 anos'.format(menor20))
