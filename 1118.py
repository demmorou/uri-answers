'''
Várias Notas Com Validação
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
        validas = 0
        soma = 0
        opcao = 0

        while opcao != 1 and opcao != 2:
            print("novo calculo (1-sim 2-nao)")
            opcao = int(input())

        if opcao == 2:
            break
    