"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
"""

nome = '-1'
while nome != '-1':
    nome = input('Digite o nome do Atleta: ')
    if nome != '-1':
        primeiro_salto = float(input('Primeiro Salto: '))
        segundo_salto = float(input('Segundo Salto: '))
        terceiro_salto = float(input('Terceiro Salto: '))
        quarto_salto = float(input('Quarto Salto: '))
        quinto_salto = float(input('Quinto Salto: '))
        media = (primeiro_salto + segundo_salto + terceiro_salto + quarto_salto + quinto_salto) / 5
        print(f'Atleta: {nome}\n'
        f'\n'
        f'Primeiro Salto: {primeiro_salto}')
