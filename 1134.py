'''
Tipo de Combustível
'''

combustiveis = {
    "1": 0,
    "2": 0,
    "3": 0
}


while True:
    opcao = int(input())

    if opcao == 4:
        print("MUITO OBRIGADO")
        print(f'Alcool: {combustiveis["1"]}')
        print(f'Gasolina: {combustiveis["2"]}')
        print(f'Diesel: {combustiveis["3"]}')
        break
    elif opcao >= 1 and opcao <= 3:
        combustiveis[str(opcao)] += 1
    