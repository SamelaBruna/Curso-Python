larg = float(input('Largura da parede: '))
Alt =  float(input('Altura da parede: '))
area = larg * Alt
print('Sua parede tem a dimensão de {}x{} e sua é de {} m²'.format(larg,Alt,area))
print('Para pintar essa parede, você precisará de {} litros '.format(area/2))