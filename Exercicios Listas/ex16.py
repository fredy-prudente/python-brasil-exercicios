"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470.
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:

    $200 - $299
    $300 - $399
    $400 - $499
    $500 - $599
    $600 - $699
    $700 - $799
    $800 - $899
    $900 - $999
    $1000 em diante

"""
vendas = 0
recebidos = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while vendas != -1:
    vendas = float(input('Quanto vendeu em uma semana: R$'))
    if vendas != -1:
        recebe = (vendas * 0.09) + 200
        if 200 <= recebe <= 299:
            recebidos[0] = +1
        elif 300 <= recebe <= 399:
            recebidos[1] = +1
        elif 400 <= recebe <= 499:
            recebidos[2] = +1
        elif 500 <= recebe <= 599:
            recebidos[3] = +1
        elif 600 <= recebe <= 699:
            recebidos[4] = +1
        elif 700 <= recebe <= 799:
            recebidos[5] = +1
        elif 800 <= recebe <= 899:
            recebidos[6] = +1
        elif 900 <= recebe <= 999:
            recebidos[7] = +1
        else:
            recebidos[8] = +1
print(recebidos)
