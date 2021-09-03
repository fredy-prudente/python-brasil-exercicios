"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

temperaturas = []
meses_extenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
                 "Novembro", "Dezembro"]
acima_media_anual = []
for i in range(12):
    temperatura = int(input(f'Digite a temperatura média do mês {i+1}: '))
    temperaturas.append(temperatura)

media = sum(temperaturas)/len(temperaturas)

print(f'Média das temperaturas: {media:.2f}')
print('Temperaturas acima da média anual:')
for i in range(12):
    if temperaturas[i] > media:
        print(temperaturas[i])
        acima_media_anual.append(f'{i+1} - {meses_extenso[i]}')

print(f'Mês que elas ocorrem:\n{acima_media_anual}')
