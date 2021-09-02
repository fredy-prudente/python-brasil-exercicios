"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o
valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
total = 0
quantidadecds = int(input('Quantidades de CDs: '))
for i in range(quantidadecds):
    valor = int(input(f'Valor pago no CD {i+1} R$'))
    total += valor
print(f'Total investido: R${total:.2f}')
print(f'Valor médio gasto em cada CD: R${(total/quantidadecds):.2f}')
