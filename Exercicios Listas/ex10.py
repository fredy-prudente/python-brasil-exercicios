"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

vetorA = []
vetorB = []
vetorC = []

for i in range(10):
    vetorA.append(int(input('Digite elemento para o vetor A: ')))
for i in range(10):
    vetorB.append(int(input('Digite elemento para o vetor B: ')))
for i in range(10):
    vetorC.append(vetorA[i])
    vetorC.append(vetorB[i])

print(vetorC)
