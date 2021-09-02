"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes
da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário
digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente
mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
"""

codigo = 1
maisbaixo = 100
maismagro = 10000000
maisalto = codigomaisalto = codigomaisbaixo = maisgordo = codigomaisgordo = codigomaismagro = alturas = pesos = \
    quantidade = 0

while codigo != 0:
    codigo = int(input('Digite seu código: '))
    if codigo != 0:
        altura = float(input('Digite sua altura: '))
        peso = int(input('Digite seu peso: '))
        alturas += altura
        pesos += peso
        quantidade += 1
        if altura > maisalto:
            maisalto = altura
            codigomaisalto = codigo
        if altura < maisbaixo:
            maisbaixo = altura
            codigomaisbaixo = codigo
        if peso > maisgordo:
            maisgordo = peso
            codigomaisgordo = codigo
        if peso < maismagro:
            maismagro = peso
            codigomaismagro = codigo

print(f'O cliente mais alto: CODIGO {codigomaisalto} com a altura de {maisalto:.2f}')
print(f'O cliente mais baixo: CODIGO {codigomaisbaixo} com a altura de {maisbaixo:.2f}')
print(f'O cliente mais gordo: CODIGO {codigomaisgordo} com o peso de {maisgordo:.2f}')
print(f'O cliente mais magro: CODIGO {codigomaismagro} com o peso de {maismagro:.2f}')
print('=====================================================================================')
print(f'A média das alturas é: {(alturas/quantidade):.2f}')
print(f'A média dos pesos é: {(pesos/quantidade):.2f}')
