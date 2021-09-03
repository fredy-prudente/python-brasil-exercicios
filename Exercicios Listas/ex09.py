"""
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetorA = []

for i in range(10):
    vetorA.append(int(input('Digite um número: ')))

for i in range(len(vetorA)):
    print(f'Elemento {i+1}: {vetorA[i]**2}')
