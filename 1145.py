'''
Sequência Lógica 2
'''

numeros = input()

x, y = numeros.split()
x = int(x)
y = int(y)

for i in range(1, y+1):
    if i % x != 0:
        print(i, end=" ")
    else:
        print(i)
