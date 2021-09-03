"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

vetorA = []
vetorB = []
vetorC = []
vetorD = []

for i in range(10):
    vetorA.append(int(input('Digite elemento para o vetor A: ')))
for i in range(10):
    vetorB.append(int(input('Digite elemento para o vetor B: ')))
for i in range(10):
    vetorC.append(int(input('Digite elemento para o vetor C: ')))
for i in range(10):
    vetorD.append(vetorA[i])
    vetorD.append(vetorB[i])
    vetorD.append(vetorC[i])

print(vetorD)
