"""
Em uma eleição presidencial existem quatro candidatos.
Os votos são informados por meio de código. Os códigos utilizados são:

    1 , 2, 3, 4  - Votos para os respectivos candidatos
    (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
    5 - Voto Nulo
    6 - Voto em Branco

    Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A porcentagem de votos nulos sobre o total de votos;
    A porcentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
"""

voto = -1
candidato1 = candidato2 = candidato3 = candidato4 = nulo = branco = 0
while voto != 0:
    voto = int(input('Como declara seu voto? '))
    if voto != 0:
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 4:
            candidato4 += 1
        elif voto == 5:
            nulo += 1
        elif voto == 6:
            branco += 1
total = candidato1 + candidato2 + candidato3 + candidato4 + nulo + branco
porcentagemnulos = (nulo / total) * 100
porcentagembrancos = (branco / total) * 100

print(f'RESULTADO!\n'
      f'Candidato 1: {candidato1} votos.\n'
      f'Candidato 2: {candidato2} votos.\n'
      f'Candidato 3: {candidato3} votos.\n'
      f'Candidato 4: {candidato4} votos.\n'
      f'Nulos: {nulo} votos.\n'
      f'Brancos: {branco} votos.\n'
      f'====================================\n'
      f'Total de votos: {total} votos.\n'
      f'Porcentagem de votos nulos sobre o total de votos: {porcentagemnulos:.2f}%\n'
      f'Porcentagem de votos brancos sobre o total de votos: {porcentagembrancos:.2f}%')


