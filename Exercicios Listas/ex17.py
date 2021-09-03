"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
ser encerrado quando não for informado o nome do atleta. A saída do programa 
deve ser conforme o exemplo abaixo: 
"""

nome = '0'
nomes = []
primeirosaltos = []
segundosaltos = []
terceirosaltos = []
quartosaltos = []
quintosaltos = []
medias = []
while nome != '-1':
    nome = input('Digite o nome do Atleta: ')
    if nome != '-1':
        nomes.append(nome)
        primeirosalto = float(input('Primeiro Salto: '))
        primeirosaltos.append(primeirosalto)
        segundosalto = float(input('Segundo Salto: '))
        segundosaltos.append(segundosalto)
        terceirosalto = float(input('Terceiro Salto: '))
        terceirosaltos.append(terceirosalto)
        quartosalto = float(input('Quarto Salto: '))
        quartosaltos.append(quartosalto)
        quintosalto = float(input('Quinto Salto: '))
        quintosaltos.append(quintosalto)
        media = (primeirosalto + segundosalto +
                 terceirosalto + quartosalto + quintosalto) / 5
        medias.append(media)
print(f'Resultado Final:\n')
for i in range(len(nomes)):
    print(f'Atleta: {nomes[i]}\n'
          f'Saltos: {primeirosaltos[i]} - {segundosaltos[i]} - {terceirosaltos[i]} - {quartosaltos[i]} - '
          f'{quintosaltos[i]}\n'
          f'Média dos saltos: {medias[i]:.2f} m')
