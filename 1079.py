'''
Médias Ponderadas
'''

n = int(input())

soma_dos_pesos = 2 + 3 + 5

for i in range(n):
    x = input().split()
    a, b, c = x

    somatorio = (float(a) * 2) + (float(b) * 3) + (float(c) * 5)

    media_ponderada = somatorio / soma_dos_pesos

    print("{0:.1f}".format(media_ponderada))