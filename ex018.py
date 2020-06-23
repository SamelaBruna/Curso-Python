from math import cos, sin, tan, radians
ang = float(input('Digite o angulo desejado em GRAUS: '))
ang = radians(ang)
print('O angulo de {} tem o SENO de :{:.2f}'.format(ang, sin(ang)))
print('O angulo de {} tem o COSSENO de :{:.2f}'.format(ang, cos(ang)))
print('O angulo de {} tem o TANGENTE de :{:.2f}'. format(ang, tan(ang)))
