'''
Crescente e Decrescente
'''

while True:
    a = input().split()
    x, y = a

    x = int(x)
    y = int(y)

    if x == y:
        break

    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
