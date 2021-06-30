'''
Resto da Divisão
'''

x = int(input())
y = int(input())

maior = x
menor = y

if x > y:
    maior = x
    menor = y
elif y > x:
    maior = y
    menor = x

for i in range(menor+1, maior):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
