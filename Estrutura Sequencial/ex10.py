# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = int(input('Digite a temperatura em Celsius: '))
f = (c * 9/5) + 32
print(f'{c} Celsius foi transformado em {f:.2f} Fahrenheit')
