"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
informados também pelo usuário.
"""

tabuada = int(input('Montar a tabuada de: '))
start = int(input('Começar por: '))
end = int(input('Terminar por: '))
contador = 0

while end < start:
    end = int(input('Terminar por: '))

print(f'Vou montar a tabuada de {tabuada} começando em {start} e terminando em {end}:')
for i in range(end - start + 1):
    print(f'{tabuada} X {start + contador} = {tabuada * (start + contador)}')
    contador += 1
