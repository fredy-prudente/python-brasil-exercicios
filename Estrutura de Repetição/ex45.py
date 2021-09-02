"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
vai utilizar o sistema. Após todos os alunos terem respondido informar:

    Maior e Menor Acerto;
    Total de Alunos que utilizaram o sistema;
    A Média das Notas da Turma.
"""
questao01 = 'F'
acerto = 0
maior = 0
alunos = 0
totalacertos = 0
menor = 11
while questao01 != '0':
    acerto = 0
    alunos += 1
    questao01 = input('Questão 01: ').upper()
    if questao01 == 'A' or questao01 == 'B' or questao01 == 'C' or questao01 == 'D' or questao01 == 'E':
        if questao01 == 'A':
            acerto += 1
        questao02 = input('Questão 02: ').upper()
        if questao02 == 'B':
            acerto += 1
        questao03 = input('Questão 03: ').upper()
        if questao03 == 'C':
            acerto += 1
        questao04 = input('Questão 04: ').upper()
        if questao04 == 'D':
            acerto += 1
        questao05 = input('Questão 05: ').upper()
        if questao05 == 'E':
            acerto += 1
        questao06 = input('Questão 06: ').upper()
        if questao06 == 'E':
            acerto += 1
        questao07 = input('Questão 07: ').upper()
        if questao07 == 'D':
            acerto += 1
        questao08 = input('Questão 08: ').upper()
        if questao08 == 'C':
            acerto += 1
        questao09 = input('Questão 09: ').upper()
        if questao09 == 'B':
            acerto += 1
        questao10 = input('Questão 10: ').upper()
        if questao10 == 'A':
            acerto += 1

        if acerto > maior:
            maior = acerto
        if acerto < menor:
            menor = acerto

        totalacertos += acerto
media = totalacertos / alunos

print(f'A maior nota foi: {maior}')
print(f'A menor nota foi: {menor}')
print(f'Total de alunos: {alunos}')
print(f'Média das notas: {media}')
