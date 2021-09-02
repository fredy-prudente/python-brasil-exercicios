"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

par = []
impar = []
numeros = []


def numero_par(n):
    if n % 2 == 0:
        return True
    else:
        return False


for i in range(20):
    numero = int(input(f'Digite o {i + 1} número: '))
    numeros.append(numero)
    if numero_par(numero):
        par.append(numero)
    else:
        impar.append(numero)


print(f'Numeros: {numeros}\n'
      f'Impares: {impar}\n'
      f'Pares: {par}')
