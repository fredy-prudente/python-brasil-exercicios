"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
numeros = []
for i in range(10):
    n = float(input('Digite um número: '))
    numeros.append(n)
print(numeros[::-1])
