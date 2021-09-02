# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

semanas = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

for i in range(0, 1, 1):
    dia = int(input('Digite o número do dia: '))
    if dia == 1:
        dia = dia - 1
        print(semanas[dia])
    elif 1 < dia <= 6:
        dia = dia - 1
        print(semanas[dia])
    else:
        print('Valor inválido!')
