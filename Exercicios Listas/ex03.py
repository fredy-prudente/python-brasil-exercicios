"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

for i in range(4):
    nota = float(input(f'Digite a {i+1} nota: '))
    notas.append(nota)
print(f'Nota 1: {notas[0]}\n'
      f'Nota 2: {notas[1]}\n'
      f'Nota 3: {notas[2]}\n'
      f'Nota 4: {notas[3]}\n'
      f'Média: {sum(notas)/len(notas)}')
