# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que deverá pagar
# Imprima os dados do programa com as mensagens adequadas

quilos = float(input('Quantidade de kilos de peixes: '))
if quilos > 50:
    multa = (quilos - 50) * 4
    print(f'Passou do limite! Excesso de {(quilos - 50):.2f} quilos de peixe! Terá que pagar o valor de R${multa:.2f}')
else:
    print(f'Você está dentro do limite! Está tudo em conforme...')
