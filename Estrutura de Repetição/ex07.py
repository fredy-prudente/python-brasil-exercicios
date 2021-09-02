"""
Faça um programa que leia 5 números e informe o maior número.
"""
numeros = []

for i in range(0, 5, 1):
    n = int(input('Digite um número: '))
    numeros.append(n)
print(f'O maior número é: {max(numeros)}')
