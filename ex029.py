print('RADAR ELETRÔNICO! ')
vel = int(input('Velocidade do carro: '))
if vel > 80:
    multa = (vel - 80)* 7.00
    print('Sua velocidade ultrapassou os 80km/h, você foi multado, sua multa é de R$ {:.2f} '.format(multa))
else:
    print('Sua velocidade foi de {}km/h'.format(vel))