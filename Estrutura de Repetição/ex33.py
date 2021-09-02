"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""
temperatura = 1
soma = 0
quantidade = 0
maior = 0
menor = 0
while temperatura != 0:
    temperatura = float(input('Digite a temperatura: [0 para parar] '))
    if temperatura != 0:
        soma += temperatura
        quantidade += 1
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
print(f'Maior: {maior}')
print(f'Menor: {menor}')
print(f'Média: {soma/quantidade}')
