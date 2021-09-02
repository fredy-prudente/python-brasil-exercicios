"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

numero = int(input("Digite um número: "))
contador2 = numero - 1
fatorial = 0
for i in range(0, numero - 1):
    fatorial = numero * contador2
    numero = fatorial
    contador2 = contador2 - 1
print(f'O Fatorial é: {fatorial}')

