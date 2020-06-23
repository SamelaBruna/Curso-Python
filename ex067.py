num = 0
while num >= 0:
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    print('-' * 20)
    for c in range(1, 11): #for que vai de 1 a 10
        print('{} x {} = {} '.format(num, c, num * c))
    print('-' * 20)
print('PROGRAMA ENCERRADO, VOLTE SEMPRE!!')
