sum = 0
for c in range (0,6):
    num = int(input('Digite o {}° número: '.format(c+1)))
    if num % 2 == 0:
        sum += num
    else:
        sum += 0
print('A soma dos numeros pares é ', sum)
