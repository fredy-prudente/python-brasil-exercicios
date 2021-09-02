"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
"""
juros = 0
valorparcela = 0
v = False
divida = float(input('Digite o valor da dívida: R$'))
parcelas = int(input('Quantidade de parcelas: '))

while not v:
    if parcelas == 1:
        juros = 0
        v = True
    elif parcelas == 2:
        juros = 5/100
        v = True
    elif parcelas == 3:
        juros = 10/100
        v = True
    elif parcelas == 6:
        juros = 15/100
        v = True
    elif parcelas == 9:
        juros = 20/100
        v = True
    elif parcelas == 12:
        juros = 25/100
        v = True
    else:
        print('Parcelas entre 1x, 2x, 3x, 6x, 9x e 12x!')
        parcelas = float(input('Quantidade de parcelas: '))
montante = divida * (1+juros) ** parcelas

print('Valor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor da Parcela')
print(f'R${divida}               {juros}%                  {parcelas}                    {valorparcela}')
print(f'{montante:.2f}')
