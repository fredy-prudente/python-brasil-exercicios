# Faça um Programa que leia três números e mostre-os em ordem decrescente.

listadecresecente = []

for i in range(0, 3, 1):
    n = float(input('Digite um número: '))
    listadecresecente.append(n)
print(sorted(listadecresecente))
