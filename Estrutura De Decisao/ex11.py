"""
    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
    baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.

"""

salario = int(input('Digite seu salário: R$'))
porcetagem = 0
aumento = 0
nsalario = 0
if salario <= 280:
    aumento = salario * 20/100
    porcetagem = 20
    nsalario = salario + aumento

elif salario <= 700:
    aumento = salario * 15/100
    porcetagem = 15
    nsalario = salario + aumento

elif salario <= 1500:
    aumento = salario * 10/100
    porcetagem = 10
    nsalario = salario + aumento

elif salario > 1500:
    aumento = salario * 5/100
    porcetagem = 5
    nsalario = salario + aumento

print(f'Seu salário de R${salario:.2f} recebeu um aumento de {porcetagem}% aumentando em R${aumento:.2f} sendo o novo salario de R${nsalario:.2f}')
