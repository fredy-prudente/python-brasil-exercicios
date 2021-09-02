"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
"""
notas = []
atleta = input('Atleta: ')
for i in range(1, 8):
    nota = float(input(f'Nota {i}: '))
    notas.append(nota)
print('Resultado Final:')
print(f'Atleta: {atleta}')
print(f'Melhor nota: {max(notas)}')
print(f'Pior nota: {min(notas)}')
print(f'Média: {(sum(notas) - max(notas) - min(notas))/5}')
