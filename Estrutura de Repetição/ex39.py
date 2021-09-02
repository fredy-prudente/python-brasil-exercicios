"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

numero = 1
maisalto = 0
numeroalto = 0
numeromenor = 0
menor = 100000
while numero != 0:
    numero = int(input('Digite o codigo do aluno: '))
    if numero != 0:
        altura = int(input('Digite a altura do aluno em cm: '))
        if altura > maisalto:
            numeroalto = numero
            maisalto = altura
        if altura < menor:
            numeromenor = numero
            menor = altura
print(f'Aluno mais alto: \nCODIGO: {numeroalto} ALTURA: {maisalto}')
print(f'Aluno mais baixo: \nCODIGO: {numeromenor} ALTURA: {menor}')
