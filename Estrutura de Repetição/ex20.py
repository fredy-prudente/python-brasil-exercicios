"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""


numero = int(input("Digite um número: "))
contador2 = numero - 1
fatorial = 0
while numero != 0:
    if 16 > numero > 0:
        for i in range(0, numero - 1):
            fatorial = numero * contador2
            numero = fatorial
            contador2 = contador2 - 1
            print(f'O Fatorial é: {fatorial}')
            numero = int(input("Digite um número: "))


