"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

numeros = []
numero = 1

while numero != 0:
    numero = int(input('Digite um número de 1 a 1000: [Digite 0 para parar] '))
    if 1000 >= numero >= 1:
        numeros.append(numero)

    elif numero != 0:
        numero = int(input('Digite um número VÁLIDO de 1 a 1000: [Digite 0 para parar] '))
        if 1000 >= numero >= 1:
            numeros.append(numero)

    if numero == 0:
        numero = 0


print(f'O menor número digitado foi {min(numeros)}\n'
      f'O maior número digitado foi {max(numeros)}\n'
      f'A soma entre os numeros é {sum(numeros)}')
