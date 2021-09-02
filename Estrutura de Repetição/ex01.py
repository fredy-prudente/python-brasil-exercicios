"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

n = float(input("informe um numero de 0 a 10: "))

while (n > 10) or (n < 0):
    n = float(input("informe um numero de 0 a 10: "))
print('Você digitou o valor correto :)')
