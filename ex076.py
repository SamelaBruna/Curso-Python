tupla = ('Lápis',1.70,'Borracha',2,'Caderno', 15.90, 'Estojo',25,'Transferidor',4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print("="*50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("="*50)

for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end = '') #alinhado a esquerda e completa com os pontos
    else:
        print(f'R${tupla[i]:>7.2f}')
print("="*50)