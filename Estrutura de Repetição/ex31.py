"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
"""

compra = 1
contador = 0
total = 0
for i in range(1):
    print('Lojas Tabajara')
while compra != 0:
    if compra > 0:
        contador += 1
        compra = float(input(f'Produto {contador}: R$'))
        total += compra
    else:
        break
print(f'Total: R${total:.2f}')
dinheiro = float(input('Dinheiro: R$'))
print(f'Troco: R${dinheiro-total:.2f}')

