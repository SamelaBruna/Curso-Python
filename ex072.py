numeros = ('zero','um','dois','três', 'quatro', 'cinco', 'seis' , 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis' ,'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero entre 0 e 20: '))
while num > 20 or num < 0:
    num = int(input('Digite novamente: '))
print(f'Você digitou o número {numeros[num]}')