from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if (inicio > fim):
        contagem = inicio
        while (contagem >= fim):
            print(f'{contagem}', end=' ')
            contagem -= passo
            sleep(0.5)
        print('FIM')
        print('--'*20)
    else:
        contagem = inicio
        while (contagem <= fim):
            print(f'{contagem}', end=' ')
            contagem += passo
            sleep(0.5)
        print('FIM')
        print('--'*20)


contador(1, 10, 1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)

