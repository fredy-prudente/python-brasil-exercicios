"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

respostas = []
positivo = 0

print('Responda as perguntas usando S ou N.')
respostas.append(input('Telefonou para a vítima? ').upper())
respostas.append(input('Esteve no local do crime? ').upper())
respostas.append(input('Mora perto da vítima? ').upper())
respostas.append(input('Devia para a vítima? ').upper())
respostas.append(input('Já trabalhou com a vítima? ').upper())

for i in range(5):
    if 'S' in respostas[i]:
        positivo += 1

if positivo == 5:
    print(f'Classificação de participação: Assassino!')
elif positivo == 3 or positivo == 4:
    print(f'Classificação de participação: Cúmplice!')
elif positivo == 2:
    print(f'Classificação de participação: Suspeita!')
else:
    print(f'Classificação de participação: Inocente!')
