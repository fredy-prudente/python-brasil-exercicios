"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

numeros = []
multi = 1
for i in range(5):
    n = int(input('Digite um número: '))
    multi *= n
    numeros.append(n)
print(f'Numeros: {numeros}\n'
      f'Soma: {sum(numeros)}\n'
      f'Multiplicação: {multi}')
