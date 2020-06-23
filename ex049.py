num = int(input('Digite um número: '))
print('A tabuda do {} é:'.format(num))
print('-'*20)
for c in range(1,11):
    print('{} x {} = {} '.format(num,c,num*c))
print('-'*20)