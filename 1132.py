'''
Múltiplos de 13
'''

x = int(input())
y = int(input())

soma = 0

menor = 0
maior = 0

if x > y:
  maior = x
  menor = y
elif y > x:
  maior = y
  menor = x
else:
  maior = x
  menor = y

for i in range(menor, maior+1):
  if i % 13 != 0:
    soma += i

print(soma)