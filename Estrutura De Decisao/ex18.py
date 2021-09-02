"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""

dia = int(input('Digite o dia do ano: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if dia | mes | ano <= 0:
    print('Essa não é uma data válida')
elif dia > 31:
    print('Essa não é uma data válida')
elif mes > 12:
    print('Essa não é uma data válida')
else:
    print(f'A data {dia}/{mes}/{ano} está correta!')
