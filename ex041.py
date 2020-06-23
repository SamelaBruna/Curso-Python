from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = int(date.today().year - ano)
print('Idade:',idade)
if idade <= 9:
    print('MIRIM')
elif 9 < idade <=14:
    print('INFANTIL')
elif 14 < idade <=19:
    print('JUNIOR')
elif 19 < idade <=20:
    print('SÊNIOR')
else:
    print('MASTER')
