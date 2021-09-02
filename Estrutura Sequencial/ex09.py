# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
f = int(input('Digite a temperatura em Fahrenheit: '))
c = 5 * ((f - 32)/9)
print(f'{f} Fahrenheit foi transformado em {c:.2f} Celsius')
