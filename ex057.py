sexo = str(input('Digite seu sexo [M/F]: '))
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dado inválido, digite novamente: ')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))