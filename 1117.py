'''
Validação de Nota
'''

validas = 0
soma = 0

while True:
    nota = input()

    nota = float(nota)

    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        soma += nota
        validas += 1
    
    if validas == 2:
        print("media = {:.2f}".format(soma / 2))
        break
