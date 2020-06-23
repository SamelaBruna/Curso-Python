frase = input('Digite uma frase: ').strip() #remover espaços desnecessários colocados pelo o usuario
print('A letra a ou A aparece {} vezes '. format(frase.upper().count('A')))
print('Apareceu pela primeira vez na posição: {}' . format(frase.upper().find('A') + 1))
print('Apareceu pela ultima vez na posição: {}' . format(frase.upper().rfind('A') + 1)) #procura apartir do lado direito