#Exercicio utilizando o if mas poderia usar alguma função do python como max, min. Ou criar uma lista e ordenar do maior pro menor
n1 = float(input('Primeiro número:'))
n2 = float(input('Segundo número:'))
n3 = float(input('Terceiro número:'))
if (n1 > n2 and n1 > n3):
    print('{} é o maior'.format(n1))
    if(n2 > n3):
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n2))
if (n2 > n1 and n2 > n3):
    print('{} é o maior'.format(n2))
    if(n1 > n3):
        print('{} é o menor'.format(n3))
    else:
        print('{} é o menor'.format(n1))
if (n3 > n1 and n3 > n2):
    print('{} é o maior'.format(n3))
    if(n2 > n1):
        print('{} é o menor'.format(n1))
    else:
        print('{} é o menor'.format(n2))