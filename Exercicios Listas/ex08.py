"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idades = []
alturas = []

for i in range(5):
    idades.append(int(input(f'Digite sua IDADE, pessoa {i+1}: ')))
    alturas.append(float(input(f'Digite sua ALTURA, pessoa {i+1}: ')))

print(f'Idades: {idades[::-1]}\n'
      f'Alturas: {alturas[::-1]}')

