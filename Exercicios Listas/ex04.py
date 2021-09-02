"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
cont = 0
letras = []
vogais = ['a', 'e', 'i', 'o', 'u']
i = 1
while i <= 10:
    letras.append(input("Letra: "))
    i += 1
i = 0
while i <= 9:
    if letras[1] not in vogais:
        cont += 1
    i += 1
print(f"Foram lidos {cont} consoantes")
