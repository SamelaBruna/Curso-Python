num = 0
cont = 0
sum = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += 1
    sum += num
print(sum)
