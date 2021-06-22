'''
Par ou Ímpar
'''

def par(num):
    return num % 2 == 0

def positivo(num):
    return num >= 0

n = int(input())

for i in range(n):
    x = int(input())
    result = ''

    if par(x) and x != 0:
        result += 'EVEN '
    else:
        result += 'ODD '

    if positivo(x):
        result += 'POSITIVE'
    else:
        result += 'NEGATIVE'

    if x == 0:
        result = 'NULL'
    
    print(result)
