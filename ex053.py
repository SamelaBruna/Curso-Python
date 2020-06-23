frase = str(input('Digite uma frase: ')).strip()
listaPalavras = frase.upper().split()
tam = len(listaPalavras)
frase2 = ''
fraseInv = ''
for i in range (0,tam):
    frase2 += listaPalavras[i]
tam2 = len(frase2)
for c in range (tam2-1,-1,-1):
    fraseInv += frase2[c]
if frase2 == fraseInv:
    print('A frase "{}" é um palidromo'.format(frase.capitalize()))
else:
    print('A frase "{}" NÃO é um palidromo'.format(frase.capitalize()))



