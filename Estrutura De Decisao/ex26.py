"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    a. Álcool:
    b. até 20 litros, desconto de 3% por litro
    c. acima de 20 litros, desconto de 5% por litro
    d. Gasolina:
    e. até 20 litros, desconto de 4% por litro
    f. acima de 20 litros, desconto de 6% por litro

    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
    (codificado da seguinte forma: A-álcool, G-gasolina),
    calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50
    o preço do litro do álcool é R$ 1,90.
"""

litros = int(input('Quantidade de litros colocado? '))
forma = input('Álcool ou Gasolina? (A-álcool, G-gasolina) ').upper()
precolitro = 0
preco = 0

if forma == 'A':
    if litros <= 20:
        precolitro = 1.843
        preco = litros * precolitro
        print(f'O valor a ser pago será de R${preco:.2f}, sendo colocado {litros} litros de álcool.')
    elif litros > 20:
        precolitro = 1.805
        preco = litros * precolitro
        print(f'O valor a ser pago será de R${preco:.2f}, sendo colocado {litros} litros de álcool.')
elif forma == 'G':
    if litros <= 20:
        precolitro = 2.4
        preco = litros * precolitro
        print(f'O valor a ser pago será de R${preco:.2f}, sendo colocado {litros} litros de gasolina.')
    elif litros > 20:
        precolitro = 2.35
        preco = litros * precolitro
        print(f'O valor a ser pago será de R${preco:.2f}, sendo colocado {litros} litros de gasolina.')
