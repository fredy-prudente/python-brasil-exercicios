"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
classificacao = 0
print('Utilize s para sim e n para não em todas as respostas!')
p1 = input('Telefonou para a vítima? ').lower()
if p1 == 's':
    classificacao += 1
p2 = input('Esteve no local do crime? ').lower()
if p2 == 's':
    classificacao += 1
p3 = input('Mora perto da vítima? ').lower()
if p3 == 's':
    classificacao += 1
p4 = input('Devia para a vítima? ').lower()
if p4 == 's':
    classificacao += 1
p5 = input('Já trabalhou com a vítima? ').lower()
if p5 == 's':
    classificacao += 1

if classificacao == 2:
    print('Você é um SUSPEITO do caso!')
elif 2 < classificacao < 5:
    print('Você é um CÚMPLICE do caso!')
elif classificacao == 5:
    print('Você é um ASSASSINO do caso!')
else:
    print('Você é INOCENTE do caso!')
