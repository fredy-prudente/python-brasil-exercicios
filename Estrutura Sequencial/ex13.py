# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#
#     Para homens: (72.7*h) - 58
#     Para mulheres: (62.1*h) - 44.7

s = str(input('Homem ou mulher? Utilize H ou F ')).upper()
al = float(input('Digite sua altura: '))

if s == 'H':
    print(f'Seu peso ideal é {((72.7 * al) - 58):.2f}')
elif s == 'F':
    print(f'Seu peso ideal é {((62.1 * al) - 44.7):.2f}')
else:
    print('Não digitou corretamente o sexo da pessoa.')
