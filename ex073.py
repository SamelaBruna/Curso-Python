times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia',
         'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará','Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('--'*135)
print('Lista de times do Brasileirão:',times)
print('--'*135)
print('Os 5 primeiros são:', times[:5])
print('--'*135)
print('Os 4 ultimos são: ',times[-4:])
print('--'*135)
print('Times em ordem alfabética', sorted(times))
print('--'*135)
print('O Chapecoense está na {}° posição.'.format(times.index('Chapecoense')+1))