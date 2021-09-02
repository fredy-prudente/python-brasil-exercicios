# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato.

listaprodutos = []

for i in range(0, 3, 1):
    p = float(input('Qual é o preço do produto? R$'))
    listaprodutos.append(p)
print(f'O produto que você deve comprar é o de R${min(listaprodutos):.2f}')
