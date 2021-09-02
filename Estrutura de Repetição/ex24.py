"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""

n = 0
contador = 0
soma = 0
while n != -1:
    n = float(input('Digite um número: [Digite -1 para parar] '))
    if n > -1:
        soma += n
        contador += 1
print(f'A média aritmética desses {contador} números é {(soma/contador):.2f}')
