"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
"""

habpaisA = int(input('Digite a quantidade de habitantes do país A: '))
taxaA = float(input('Taxa de crescimento do país A: (em %) '))
habpaisB = int(input('Digite a quantidade de habitantes do país B: '))
taxaB = float(input('Taxa de crescimento do país B: (em %) '))
ano = 0
print(f'População:\n'
      f'País A: {habpaisA:.0f}\n'
      f'País B: {habpaisB:.0f}\n'
      f'Ano atual: {ano}')

while habpaisA <= habpaisB:
    habpaisA = habpaisA + (habpaisA * (taxaA / 100))
    habpaisB = habpaisB + (habpaisB * (taxaB / 100))
    ano += 1
    print('=====================')
    print(f'População:\n'
          f'País A: {habpaisA:.0f}\n'
          f'País B: {habpaisB:.0f}\n'
          f'Ano: {ano}')
