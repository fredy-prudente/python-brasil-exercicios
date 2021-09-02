"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
maiorindice = 0
codigomaiorindice = 0
menorindice = 1000000000
codigomenorindice = 0
quantidade = 0
veiculos2000 = 0
totalveiculos = 0
for i in range(5):
    codigo = input('Código da cidade: ')
    veiculos = int(input('Número de veiculos de passeio: '))
    acidentes = int(input('Número de acidentes de trânsito com vítimas: '))
    indice = (acidentes/veiculos) * 100
    totalveiculos += veiculos
    if indice > maiorindice:
        maiorindice = indice
        codigomaiorindice = codigo
    if indice < menorindice:
        menorindice = indice
        codigomenorindice = codigo
    if veiculos < 2000:
        quantidade += 1
        veiculos2000 += acidentes
mediaveiculos = totalveiculos/5

print(f'Cidade com MAIOR índice de acidentes de transito é: CODIGO: {codigomaiorindice} ÍNDICE {maiorindice:.2f}%')
print(f'Cidade com MENOR índice de acidentes de transito é: CODIGO: {codigomenorindice} ÍNDICE {menorindice:.2f}%')
print(f'A média de veículos nas cinco cidades juntos é: {mediaveiculos}')
print(f"A média de acidentes de trânsito nas cidades com menos de 2000 veículos é: {veiculos2000/quantidade:.2f}")
