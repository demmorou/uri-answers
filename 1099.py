'''
Soma de Ímpares Consecutivos II
'''

n = int(input())

for _ in range(n):
    a = input().split()
    x, y = a
    x = int(x)
    y = int(y)

    maior = 0
    menor = 0

    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    
    soma_impares = 0

    for i in range(menor+1, maior):
        if i % 2 != 0:
            soma_impares += i

    print(soma_impares)