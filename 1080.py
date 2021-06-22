'''
Maior e Posição
'''

numbers = []

maior = 0
posicao = 0

for i, index in enumerate(range(1, 101)):
    x = int(input())
    numbers.append(x)

    if x > maior:
        maior = x
        posicao = index

print(maior)
print(posicao)