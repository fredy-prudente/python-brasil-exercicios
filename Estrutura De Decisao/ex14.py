# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media >= 9:
    print(f'Sua média foi {media:.2f} APROVADO, nota concedida como A')
elif media >= 7.5 or media > 9:
    print(f'Sua média foi {media:.2f} APROVADO, nota concedida como B')
elif media >= 6.0 or media > 7.5:
    print(f'Sua média foi {media:.2f} APROVADO, nota concedida como C')
elif media >= 4.0 or media > 6.0:
    print(f'Sua média foi {media:.2f} REPROVADO, nota concedida como D')
elif media < 4:
    print(f'Sua média foi {media:.2f} REPROVADO, nota concedida como E')
