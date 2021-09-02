"""
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
impar = 0
par = 0

for i in range(0, 10, 1):
    n = int(input('Digite um número inteiro: '))
    if n % 2 != 0:
        impar += 1
    else:
        par += 1
print(f'A quantidade de números pares é {par} e impar é {impar}')
