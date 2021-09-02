"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg)
    de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morangos = int(input('Digite a quantidade de morangos em Kg: '))
precomorango = 2.50
maca = int(input('Digite a quantidade de maçãs em Kg: '))
precomaca = 1.80

if morangos > 5:
    precomorango = 2.20
if maca > 5:
    precomaca = 1.50

total = (precomorango * morangos) + (precomaca * maca)
if total > 25:
    total = total - (total * 0.10)

print(f'Comprado {morangos} kg de morangos pagará R${precomorango} por cada um\n'
      f'Comprando {maca} kg de maçã pagará R${precomaca} por cada um\n'
      f'Total da compra R${total}')
