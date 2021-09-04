"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de
programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
"""
voto = 1
votos = []
quantidade_votos = []
print('Enquete: Quem foi o melhor jogador?')

while voto != 0:
    voto = int(input('Número do jogador (0=fim): '))
    if voto != 0:
        if 1 <= voto <= 23:
            votos.append(voto)
        else:
            print('Informe um valor entre 1 e 23 ou 0 para sair!')


for i in range(len(votos)+23):
    quantidade_votos.append(votos.count(i+1))
print(votos)
print(quantidade_votos)
print(f'Resultado da votação:\n'
      f'Foram computados {len(votos)} votos.\n'
      f'Jogador     Votos')
for i in range(24):
    if quantidade_votos[i+1] >= 1:
        print(f'{i+1}       {quantidade_votos[i]}')
