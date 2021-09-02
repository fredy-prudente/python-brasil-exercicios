# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ['a', 'e', 'i', 'o', 'u']

letra = input('Digite uma letra: ')

if letra in vogal:
    print('Sua letra é vogal!')
else:
    print('Sua letra é consoante!')
