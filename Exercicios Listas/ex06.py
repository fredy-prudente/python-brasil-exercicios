"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""

medias = []
medias_maiores_que_sete = []

for alunos in range(10):
    n1 = float(input(f'Digite a PRIMEIRA nota do aluno {alunos+1}: '))
    n2 = float(input(f'Digite a SEGUNDA nota do aluno {alunos + 1}: '))
    n3 = float(input(f'Digite a TERCEIRA nota do aluno {alunos + 1}: '))
    n4 = float(input(f'Digite a QUARTA nota do aluno {alunos + 1}: '))
    media = (n1+n2+n3+n4) / 4
    medias.append(media)
    if media >= 7:
        medias_maiores_que_sete.append(media)
print(f'{medias}')
print(f'Números de alunos com média maior ou igual a 7.0 é: {len(medias_maiores_que_sete)}')

