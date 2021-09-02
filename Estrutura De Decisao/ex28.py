"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
    porém não há limites para a quantidade de carne por cliente.
    Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
    contendo as informações da compra:
    tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
pduplo = 4.9
palcatra = 5.9
ppicanha = 6.9
total = 0
tipocarne = input('Tipos de Carnes disponíveis:\n'
                  'a. File Duplo\n'
                  'b. Alcatra\n'
                  'C. Picanha\n').lower()
quantidade = int(input('Digite a quantidade em kilos de carne que deseja comprar: '))
formap = input('Pagamento no cartão Tabajara? (Digite s ou n)\n').lower()

if quantidade > 5:
    pduplo = 5.8
    palcatra = 6.8
    ppicanha = 7.8

if tipocarne == 'a':
    total = (quantidade * pduplo)
    desconto = total * 0.05
    totalpagar = total - desconto
    if formap == 's':
        print(f'CUPOM FISCAL\n'
              f'Carne: File Duplo\n'
              f'Quantidade: {quantidade}kg\n'
              f'Preço Total: R${total}\n'
              f'Tipo de Pagamento: Cartão Tabajara\n'
              f'Desconto: R${desconto:.2f}\n'
              f'Valor a pagar: R${total - desconto}')
    else:
        print(f'CUPOM FISCAL\n'
              f'Carne: File Duplo\n'
              f'Quantidade: {quantidade}kg\n'
              f'Preço Total: R${total}\n'
              f'Tipo de Pagamento: Cartão Normal\n'
              f'Desconto: R$0\n'
              f'Valor a pagar: R${total}')
elif tipocarne == 'b':
    total = (quantidade * palcatra)
    desconto = total * 0.05
    totalpagar = total - desconto
    if formap == 's':
        print(f'CUPOM FISCAL\n'
              f'Carne: Alcatra\n'
              f'Quantidade: {quantidade}kg\n'
              f'Preço Total: R${total}\n'
              f'Tipo de Pagamento: Cartão Tabajara\n'
              f'Desconto: R${desconto:.2f}\n'
              f'Valor a pagar: R${total - desconto}')
    else:
        print(f'CUPOM FISCAL\n'
              f'Carne: Alcatra\n'
              f'Quantidade: {quantidade}kg\n'
              f'Preço Total: R${total}\n'
              f'Tipo de Pagamento: Cartão Normal\n'
              f'Desconto: R$0\n'
              f'Valor a pagar: R${total}')
elif tipocarne == 'c':
    total = (quantidade * ppicanha)
    desconto = total * 0.05
    totalpagar = total - desconto
    if formap == 's':
        print(f'CUPOM FISCAL\n'
              f'Carne: Picanha\n'
              f'Quantidade: {quantidade}kg\n'
              f'Preço Total: R${total}\n'
              f'Tipo de Pagamento: Cartão Tabajara\n'
              f'Desconto: R${desconto:.2f}\n'
              f'Valor a pagar: R${total - desconto}')
    else:
        print(f'CUPOM FISCAL\n'
              f'Carne: Picanha\n'
              f'Quantidade: {quantidade}kg\n'
              f'Preço Total: R${total}\n'
              f'Tipo de Pagamento: Cartão Normal\n'
              f'Desconto: R$0\n'
              f'Valor a pagar: R${total}')
