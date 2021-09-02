"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
arq = int(input('Qual é o tamanho do arquivo? (em MB) '))
vel = int(input('Qual é a velocidade da internet? (em Mbps) '))
print(f'O download do arquivo de {arq} mbs vai demorar cerca de {(arq/(vel / 8) / 60):.2f} minutos para terminar.')
