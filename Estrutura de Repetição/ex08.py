"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []

for i in range(0, 5, 1):
    n = int(input('Digite um número: '))
    numeros.append(n)
media = sum(numeros) / len(numeros)
print(f'A soma entre esses números é {sum(numeros)} e a média é {media:.2f}')
