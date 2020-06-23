peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura**2)
print('IMC: {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30<= IMC < 40:
    print('Obesidade')
elif IMC >=40:
    print('Obesidade Mórbida')