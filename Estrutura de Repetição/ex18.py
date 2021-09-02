"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""

numeros = []
numero = 1
while numero != 0:
    numero = int(input('Digite um número: [Digite 0 para parar] '))
    if numero != 0:
        numeros.append(numero)

print(f'O menor número digitado foi {min(numeros)}\n'
      f'O maior número digitado foi {max(numeros)}\n'
      f'A soma entre os numeros é {sum(numeros)}')
