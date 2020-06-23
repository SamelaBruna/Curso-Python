expressao = str(input('Digite uma expressão: '))
valido = True
par_a_fechar = 0
pAbr = expressao.count('(')
pFec = expressao.count(')')

if pAbr == pFec:
    for p in expressao:
        if p == ')' and par_a_fechar == 0:
            valido = False
            print('Fechou parênteses antes de abrir')
            break
        if p == '(':
            par_a_fechar += 1
        if p == ')':
            par_a_fechar -= 1

else:
    valido = False
    print('Quantidade de parenteses ( , ) diferente')
    if par_a_fechar > 0:
        print('Você esqueceu de fechar um parenteses')
    if valido == True:
        print('Expressão válida')
    else:
        print('expressão inválida')
