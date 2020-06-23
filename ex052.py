num = int(input('Digite um número: '))
contPrim = 0
contNotPrim = 0
if num == 2:
    print('o número {} é primo'.format(num))
else:
        for i in range (1,num+1):
            if num % i == 0:
                contPrim += 1
            else:
                contNotPrim += 1
        if contPrim == 2:
             print('O número {} é primo'.format(num))
        else:
            print('O número {} NÃO é primo'.format(num))

#print(contPrim)