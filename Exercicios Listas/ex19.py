"""
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos
valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados
num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos
concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa.
"""
voto = 1
windows_server = 0
unix = 0
linux = 0
netware = 0
macOs = 0
outros = 0


def porcetagem(total, quantidade):
    resultado = (quantidade / total) * 100
    return resultado


while voto != 0:
    voto = int(input('Qual sistema operacional você vota? '))
    if voto == 1:
        windows_server += 1
    elif voto == 2:
        unix += 1
    elif voto == 3:
        linux += 1
    elif voto == 4:
        netware += 1
    elif voto == 5:
        macOs += 1
    elif voto == 6:
        outros += 1

total = windows_server + unix + linux + netware + macOs + outros
print(f'\tSistema Operacional     Votos   %\n'
      f'Windows Server      {windows_server}      {porcetagem(total, windows_server)}\n'
      f'Unix         {unix}      {porcetagem(total, unix)}\n'
      f'Linux       {linux}           {porcetagem(total, linux)}\n'
      f'Netware     {netware}       {porcetagem(total, netware)}\n'
      f'Mac OS      {macOs}     {porcetagem(total, macOs)}\n'
      f'Outros      {outros}    {porcetagem(total, outros)}')

