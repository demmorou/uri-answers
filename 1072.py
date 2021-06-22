'''
Intervalo 2
'''

n = int(input())

count_in = 0
count_out = 0

for _ in range(n):
    x = int(input())
    if x >= 10 and x <=20:
        count_in += 1
    else:
        count_out += 1

print(count_in, 'in')
print(count_out, 'out')
