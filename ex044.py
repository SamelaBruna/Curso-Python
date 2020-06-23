print('{:=^40}'.format('LOJAS GUANABARA'))
preco = float(input('Valor da compra: R$'))
opc = int(input("""Formas de pagamento
[1] - à vista dinheiro/cheque
[2] - à vista cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão
Qual a opção: """))
if opc == 1:
    tot = preco - (preco * (10/100))
    print('O total a pagar é R${:.2f}'.format(tot))
elif opc == 2:
    tot = preco - (preco * (5 / 100))
    print('O total a pagar é R${:.2f}'.format(tot))
elif opc == 3:
    tot = preco/2
    print('O preço a pagar é R${:.2f} em 2x'.format(tot))
elif opc == 4:
    parc = int(input('Quantas parcelas?'))
    tot = (preco + (preco * (20/100)))/parc
    print('O preço a pagar é R${:.2f} em {}x'.format(tot,parc))



