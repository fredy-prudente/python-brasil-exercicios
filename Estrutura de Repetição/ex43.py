"""
O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

    Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
    Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
    Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""

codigo = 1
total = cachorro = baurusimples = bauruovo = hamburguer = cheeseburguer = refrigerante = 0
while codigo != 0:
    codigo = int(input('Código do Produto: '))
    if codigo != 0:
        if codigo == 100:
            cachorro = int(input('Quantidade do Cachorro Quente: '))
            total += 1.20 * cachorro
        elif codigo == 101:
            baurusimples = int(input('Quantidade do Bauru Simples: '))
            total += 1.30 * baurusimples
        elif codigo == 102:
            bauruovo = int(input('Quantidade do Bauru com ovo: '))
            total += 1.50 * bauruovo
        elif codigo == 103:
            hamburguer = int(input('Quantidade de Hambúrguer: '))
            total += 1.20 * hamburguer
        elif codigo == 104:
            cheeseburguer = int(input('Quantidade do Cheeseburguer: '))
            total += 1.30 * cheeseburguer
        elif codigo == 105:
            refrigerante = int(input('Quantidade do Refrigerante: '))
            total += 1.00 * refrigerante

print(f'PEDIDO!')
print(f'{cachorro} - Cachorro Quente, VALOR: R$ {cachorro * 1.20}')
print(f'{baurusimples} - Bauru Simples, VALOR: R$ {baurusimples * 1.30}')
print(f'{bauruovo} - Bauru com ovo, VALOR: R$ {bauruovo * 1.50}')
print(f'{hamburguer} - Hambúrguer, VALOR: R$ {hamburguer * 1.20}')
print(f'{cheeseburguer} - Cheeseburguer, VALOR: R$ {cheeseburguer * 1.30}')
print(f'{refrigerante} - Refrigerante, VALOR: R$ {refrigerante * 1}')
print(f'Total do pedido: R${total}')
