"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""
alunos = 0
quantidadeturmas = int(input('Digite a quantidade de turmas: '))
for i in range(quantidadeturmas):
    alunosporturma = int(input(f'Digite a quantidade de alunos na turma {i+1}: '))
    while alunosporturma > 40:
        print('A turma não pode ter mais de 40 alunos!')
        alunosporturma = int(input(f'Digite a quantidade de alunos na turma {i+1}: '))
    alunos += alunosporturma
print(f'A média de alunos por turma é {alunos/quantidadeturmas}')
