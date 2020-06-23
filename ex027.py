nomeComp = input('Digite uma frase: ').strip()
nomeComp = nomeComp.title().split()
print('Primeiro nome: ', nomeComp[0])
print('Ultimo nome: ', nomeComp[len(nomeComp)-1])