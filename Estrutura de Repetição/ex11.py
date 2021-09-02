"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.

Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = []
for i in range(n1 + 1, n2, 1):
    soma.append(i)
    print(i)
print(sum(soma))
