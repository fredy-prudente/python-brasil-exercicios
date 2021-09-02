"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou
 iguale a população do país B, mantidas as taxas de crescimento.
"""

habpaisA = 80000
habpaisB = 200000
ano = 0
print(f'População:\n'
      f'País A: {habpaisA:.0f}\n'
      f'País B: {habpaisB:.0f}\n'
      f'Ano atual: {ano}')

while habpaisA <= habpaisB:
    habpaisA = habpaisA + (habpaisA * 0.03)
    habpaisB = habpaisB + (habpaisB * 0.015)
    ano += 1
    print(f'População:\n'
          f'País A: {habpaisA:.0f}\n'
          f'País B: {habpaisB:.0f}\n'
          f'Ano: {ano}')
