from datetime import date
contMaior = 0
contMenor = 0
for i in range (0,7):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i+1)))
    idade = int(date.today().year - ano)
    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print('Maiores de Idade: {}\nMenores de idade:{}'.format(contMaior,contMenor))
