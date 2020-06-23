from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = int(date.today().year - ano)
print('Quem nasceu em {} tem {} anos em {}'. format(ano,idade,date.today().year))
if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'. format(int(date.today().year) + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    print('Seu alistamento foi em {}'.format(int(date.today().year)-(idade - 18)))
else:
    print('Voce tem que se alistar imediatamente!!')
