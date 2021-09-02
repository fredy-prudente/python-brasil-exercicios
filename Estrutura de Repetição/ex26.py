"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
candidato1 = 0
candidato2 = 0
candidato3 = 0

print('ELEIÇÃO!\n'
      '[1] Bolsonaro\n'
      '[2] Haddad\n'
      '[3] Ciro')
totaleleitores = int(input('Qual é o números total de eleitores? '))
for i in range(totaleleitores):
    voto = int(input('Em quem você vota? [1] [2] [3] '))
    if voto > 3 or voto < 1:
        print('Votou errado! Vote novamente!')
        voto = int(input('Em quem você vota? [1] [2] [3] '))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
print('\nRESULTADO DA ELEIÇÃO!')
print(f'Bolsonaro conseguiu {candidato1} votos.')
print(f'Haddad conseguiu {candidato2} votos.')
print(f'Ciro conseguiu {candidato3} votos.')
