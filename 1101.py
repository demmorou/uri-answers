'''
Sequência de Números e Soma
'''

while True:
    x = input().split()
    m, n = x

    m = int(m)
    n = int(n)

    if m <= 0 or n <= 0:
        break

    maior = 0
    menor = 0

    if m > n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m
    
    sequencia = ''
    soma = 0

    for i in range(menor, maior+1):
        sequencia += f'{i} '
        soma += i
    
    print(f'{sequencia}Sum={soma}')
