'''
Soma de Impares Consecutivos I
'''

x = int(input())
y = int(input())

if x < y:
    start = x
    end = y
else:
    start = y
    end = x

result = 0

for i in range(start+1, end):
    if i % 2 != 0:
        result += i

print(result)