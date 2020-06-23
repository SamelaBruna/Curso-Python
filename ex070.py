total = 0
nProd = 0
nProdMai1000 = 0
print('-' * 20)
print('LOJA')
print('-' * 20)
while True:
    nome = str(input('Nome do produto:'))
    preco = float(input('Preço R$:'))
    nProd += 1
    total += preco
    if nProd == 1:
        prodMenor = nome
        preMenor = preco
    if preco < preMenor:
        prodMenor = nome
        preMenor = preco
    if preco > 1000:
        nProdMai1000 += 1

    print('-' * 20)
    opc =str(input('Quer continuar?')).upper()

    while opc != 'N' and opc != 'S':
        opc = str(input('Quer continuar? [S/N]')).upper()
    if opc == 'N':
        break
print('=======FIM DO PROGRAMA=======')
print('O total da compra foi R${:.2f}\nTemos {} prdutos custando mais de R$1000\nO produto mais barato foi {} que custa R${:.2f}'.format(total,nProdMai1000,prodMenor,preMenor))