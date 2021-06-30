'''
PUM
'''

n = int(input())

count = 1

for i in range(n):
    for j in range(4):
        if count % 4 != 0:
            print(count, end=" ")
        else:
            print("PUM")
        count += 1
