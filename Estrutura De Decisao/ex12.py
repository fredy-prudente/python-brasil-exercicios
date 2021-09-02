"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20%

    Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""
valorhora = int(input('Quanto você ganha por hora? R$'))
qhoras = int(input('Quantas horas você trabalha por mês? '))
salariobruto = valorhora * qhoras
inss = salariobruto * 10 / 100
fgts = salariobruto * 11 / 100



if salariobruto <= 900:
    ir = salariobruto * 0/100
    salarioliquido = salariobruto - (ir + inss)
    print(f'Salário Bruto:          R${salariobruto:.2f}\n'
          f'(-) IR (0%):            R${ir:.2f}\n'
          f'(-) INSS (10%):         R${inss:.2f}\n'
          f'(+) FGTS (11%):         R${fgts:.2f}\n'
          f'Total de impostos:      R${(ir + inss):.2f}\n'
          f'Salário Liquido:        R${salarioliquido:.2f}')

elif salariobruto <= 1500:
    ir = salariobruto * 5/100
    salarioliquido = salariobruto - (ir + inss)
    print(f'Salário Bruto:          R${salariobruto:.2f}\n'
          f'(-) IR (5%):            R${ir:.2f}\n'
          f'(-) INSS (10%):         R${inss:.2f}\n'
          f'(+) FGTS (11%):         R${fgts:.2f}\n'
          f'Total de impostos:      R${(ir + inss):.2f}\n'
          f'Salário Liquido:        R${salarioliquido:.2f}')

elif salariobruto <= 2500:
    ir = salariobruto * 10/100
    salarioliquido = salariobruto - (ir + inss)
    print(f'Salário Bruto:          R${salariobruto:.2f}\n'
          f'(-) IR (1%):            R${ir:.2f}\n'
          f'(-) INSS (10%):         R${inss:.2f}\n'
          f'(+) FGTS (11%):         R${fgts:.2f}\n'
          f'Total de impostos:      R${(ir + inss):.2f}\n'
          f'Salário Liquido:        R${salarioliquido:.2f}')

elif salariobruto > 2500:
    ir = salariobruto * 20/100
    salarioliquido = salariobruto - (ir + inss)
    print(f'Salário Bruto:          R${salariobruto:.2f}\n'
          f'(-) IR (20%):            R${ir:.2f}\n'
          f'(-) INSS (10%):         R${inss:.2f}\n'
          f'(+) FGTS (11%):         R${fgts:.2f}\n'
          f'Total de impostos:      R${(ir + inss):.2f}\n'
          f'Salário Liquido:        R${salarioliquido:.2f}')
