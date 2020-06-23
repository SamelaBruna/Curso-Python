from random import randint
numRand = randint(0,10)
tentativa = 1
jogada = int(input('Vamos Jogar!?\nAcabei de pensar em um número entre 0 e 10, será que você consegue adivinhar? '))
while numRand != jogada:
      if jogada < numRand:
        jogada = int(input('Mais...Tente novamente: '))
        palpite += 1
      elif jogada > numRand:
        jogada = int(input('Menos...Tente novamente: '))
        palpite += 1
print('Você acertou!! Após {} tentativas'.format(palpite))