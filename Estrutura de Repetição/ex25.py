"""
Faça um programa que peça para N pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""

idade = 0
quantidade = 0
soma = 0
while idade != -1:
    idade = int(input('Digite uma idade: [-1 para parar] '))
    if idade > -1:
        quantidade += 1
        soma += idade
if (soma/quantidade) <= 25:
    print(f'Pela média das idades a turma é JOVEM!')
elif (soma/quantidade) <= 50:
    print(f'Pela média das idades a turma é ADULTA!')
elif (soma / quantidade) > 50:
    print(f'Pela média das idades a turma é IDOSA!')
print(f"Média: {(soma/quantidade):.2f}")
