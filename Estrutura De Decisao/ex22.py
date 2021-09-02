"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).
"""

n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'O número {n} é PAR!')
else:
    print(f'O número {n} é IMPAR!')
