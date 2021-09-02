"""
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo,
por quais número ele é divisível.
"""
div = []
contador = 1
num = int(input("Digite um número: "))
if num % 2 == 1:
    print("Primo")
else:
    print("Não primo")
    while num >= contador:
        if num % contador == 0:
            div.append(contador)
        contador += 1
    print(f"Os números que são divisíveis por {num} são: {div}")

