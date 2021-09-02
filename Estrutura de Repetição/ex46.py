"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos
e depois informe a média dos saltos conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não
for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
"""

atleta = '1'
primeirosalto = segundosalto = terceirosalto = quartosalto = quintosalto = melhorsalto = 0
piorsalto = 100
atletas = []
medias = []
while atleta != '0':
    atleta = input('Nome do Atleta: ')
    if atleta != '0':
        primeirosalto = float(input('Primeiro Salto: '))
        segundosalto = float(input('Segundo Salto: '))
        terceirosalto = float(input('Terceiro Salto: '))
        quartosalto = float(input('Quarto Salto: '))
        quintosalto = float(input('Quinto Salto: '))
        # MELHOR SALTO
        if primeirosalto > melhorsalto:
            melhorsalto = primeirosalto
        if segundosalto > melhorsalto:
            melhorsalto = segundosalto
        if terceirosalto > melhorsalto:
            melhorsalto = terceirosalto
        if quartosalto > melhorsalto:
            melhorsalto = quartosalto
        if quintosalto > melhorsalto:
            melhorsalto = quintosalto
        # PIOR SALTO
        if primeirosalto < piorsalto:
            piorsalto = primeirosalto
        if segundosalto < piorsalto:
            piorsalto = segundosalto
        if terceirosalto < piorsalto:
            piorsalto = terceirosalto
        if quartosalto < piorsalto:
            piorsalto = quartosalto
        if quintosalto < piorsalto:
            piorsalto = quintosalto

        media = ((primeirosalto + segundosalto + terceirosalto + quartosalto + quintosalto) - melhorsalto - piorsalto)/3
        medias.append(media)
        atletas.append(atleta)

        print(f'Atleta: {atleta}\n')
        print(f'Primeiro Salto: {primeirosalto} m')
        print(f'Segundo Salto: {segundosalto} m')
        print(f'Terceiro Salto: {terceirosalto} m')
        print(f'Quarto Salto: {quartosalto} m')
        print(f'Quinto Salto: {quintosalto} m\n')
        print(f'Melhor Salto: {melhorsalto} m')
        print(f'Pior Salto: {piorsalto} m')
        print(f'Média dos demais saltos: {media:.2f} m\n')
        melhorsalto = 0
        piorsalto = 100

print(f'Resultado Final:')
for i in range(len(atletas)):
    print(f'{atletas[i]}: {medias[i]:.2f} m')
