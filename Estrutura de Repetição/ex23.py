"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

primos = []
n = int(input('Digite um número: '))

for i in range(n+1):
    if i == 1:
        ""
    elif (i+2) % 2 == 1:
        primos.append(i)
        i += 1
print(primos)
