'''
Sequencia IJ 3
'''
i = 1
j = 7

while i <= 9:
    nextj = j + 2
    while j >= nextj - 4:
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    j = nextj