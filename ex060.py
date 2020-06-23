'''num = int(input('Calcular seu fatorial: '))
n = num
som = num
while n != 1:
    print('{} x '.format(n), end='')
    som = som  * (n-1)
    n = n - 1

print('=',som)'''

num = int(input('Calcular seu fatorial: '))
n = num
som = 0
fat = 1
while n > 0 :
    print('{}'.format(n), end='')
    print(' x ' if n > 1 else ' = ', end='')
    fat = fat * n
    n = n - 1
print(fat)

