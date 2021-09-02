# Faça um Programa que leia três números e mostre o maior e o menor deles.

listanumeros = []

for i in range(0, 3, 1):
    n = float(input('Digite um número: '))
    listanumeros.append(n)
print(f'O menor número é {min(listanumeros)}')
