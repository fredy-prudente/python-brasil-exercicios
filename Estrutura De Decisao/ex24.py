"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    a. par ou ímpar;
    b. positivo ou negativo;
    c. inteiro ou decimal.
"""

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
soma = n1 + n2
print('Operações:\na. par ou ímpar;\nb. positivo ou negativo;\nc. inteiro ou decimal. ')
opera = input('Qual operação você deseja? (Utilize a, b ou c)\n').lower()

if opera == 'a':
    if soma % 2 == 0:
        print(f'A soma entre {n1} e {n2} é {soma}, sendo PAR!')
    else:
        print(f'A soma entre {n1} e {n2} é {soma}, sendo IMPAR!')
elif opera == 'b':
    if soma < 0:
        print(f'A soma entre {n1} e {n2} é {soma}, sendo NEGATIVA!')
    else:
        print(f'A soma entre {n1} e {n2} é {soma}, sendo POSITIVA!')
elif opera == 'c':
    if soma == round(soma):
        print(f'A soma entre {n1} e {n2} é {soma}, sendo INTEIRA!')
    else:
        print(f'A soma entre {n1} e {n2} é {soma}, sendo DECIMAL!')
else:
    print('Escolha da operação invalida!')
