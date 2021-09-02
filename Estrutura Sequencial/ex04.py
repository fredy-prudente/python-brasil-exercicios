# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = []
for i in range(0, 4, 1):
    nota = float(input('Insira uma nota: '))
    notas.append(nota)
media = (sum(notas) / 4)
print(f'A média entre as 4 notas é {media}')
