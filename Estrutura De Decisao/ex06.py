# Faça um Programa que leia três números e mostre o maior deles.

listanumeros = []

for i in range(0, 3, 1):
    n = float(input('Digite um número: '))
    listanumeros.append(n)
print(f'O maior número é {max(listanumeros)}')
