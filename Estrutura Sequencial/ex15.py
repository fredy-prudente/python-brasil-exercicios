# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#
#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

gh = int(input('Quanto você ganha por hora? '))
hm = int(input('Quantas horas você trabalha por mês? '))

s = gh * hm
ir = s * 0.11
inss = s * 0.08
sin = s * 0.05
sl = s - (ir + inss + sin)

print(f'+ Salário Bruto: R$ {s:.2f}\n'
      f'- IR (11%): R$ {ir:.2f}\n'
      f'- INSS (8%): R$ {inss:.2f}\n'
      f'- Sindicato (5%): R$ {sin:.2f}\n'
      f'Salário Liquido: R$ {sl:.2f}')
