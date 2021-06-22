'''
Experiências
'''

def percentual(total, parte):
    return (100 * parte) / total

n = int(input())

cobaias = {
    'S': 0,
    'C': 0,
    'R': 0
}

total_cobaias = 0

for _ in range(n):
    x = input().split()
    qtd, cobaia = x

    total_cobaias += int(qtd)
    cobaias[cobaia] += int(qtd)

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {cobaias["C"]}')
print(f'Total de ratos: {cobaias["R"]}')
print(f'Total de sapos: {cobaias["S"]}')
print("Percentual de coelhos: {0:.2f} %".format(percentual(total_cobaias, cobaias["C"])))
print("Percentual de ratos: {0:.2f} %".format(percentual(total_cobaias, cobaias["R"])))
print("Percentual de sapos: {0:.2f} %".format(percentual(total_cobaias, cobaias["S"])))
