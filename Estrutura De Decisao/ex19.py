"""
Faça um Programa que leia um número inteiro menor que 1000 imprima a quantidade de centenas, dezenas e unidades do mesmo

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades

"""

n = int(input('Digite um numero menor que 1000: '))
strn = str(n)
ntotal = len(strn)
cs = ''
ds = ''
us = ''

if ntotal == 3:
    if strn[0] > '1':
        cs = 's'

    if strn[1] > '1':
        ds = 's'

    if strn[2] > '1':
        us = 's'
    print(f'{strn[0]} centena{cs}, {strn[1]} dezena{ds}, {strn[2]} unidade{us}.')


elif ntotal == 2:
    if strn[0] > '1':
        ds = 's'

    if strn[1] > '1':
        us = 's'
    print(f'{strn[0]} dezena{ds}, {strn[1]} unidade{us}.')


elif ntotal == 1:
    if strn[0] > '1':
        us = 's'
    print(f'{strn[0]} unidade{us}.')

else:
    print('Somente de 0 a 1000!')
