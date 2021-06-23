'''
Dividindo X por Y
'''

n = int(input())

for _ in range(n):
    valores = input().split()
    x, y = valores

    x = int(x)
    y = int(y)

    if y == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(x / y))