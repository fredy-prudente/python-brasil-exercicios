"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos.
"""
alturas = []
idades = []
alunos_13anos_pequenos = 0
for i in range(30):
    idade = int(input(f'Digite a idade do aluno {i+1}: '))
    altura = float(input(f'Digite a altura do aluno {i+1}: '))
    alturas.append(altura)
    idades.append(idade)

media = sum(alturas)/len(alturas)
for i in range(30):
    if idades[i] > 13 and alturas[i] < media:
        alunos_13anos_pequenos += 1

print(f'Média das alturas dos alunos: {media:.3f}')
print(f'Alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos é: {alunos_13anos_pequenos}')
