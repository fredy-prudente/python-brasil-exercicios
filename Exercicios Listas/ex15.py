"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""

numero = 0
numeros = []
count = 0
count2 = 0

while numero != -1:
    numero = int(input('Digite um número: [-1 para parar] '))
    if numero != -1:
        numeros.append(numero)

media = sum(numeros)/len(numeros)


print(f'Mostre a quantidade de valores que foram lidos: {len(numeros)}\n'
      f'Exiba todos os valores na ordem em que foram informados, um ao lado do outro: {numeros}\n'
      f'Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro:')
for i in reversed(numeros):
    print(i)
print(f'Calcule e mostre a soma dos valores: {sum(numeros)}\n'
      f'Calcule e mostre a média dos valores: {media:.2f}')
for i in range(len(numeros)):
    if numeros[i] > media:
        count += 1
    if numeros[i] < 7:
        count2 += 1
print(f'Calcule e mostre a quantidade de valores acima da média calculada: {count}\n'
      f'Calcule e mostre a quantidade de valores abaixo de sete: {count2}\n'
      f'Mensagem: ACABOUUUU!')
