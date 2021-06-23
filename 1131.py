'''
Grenais
'''

vitorias = {
    "inter": 0,
    "gremio": 0,
    "empates": 0
}

jogos = 0

while True:
    gols = input().split()
    gols_inter, gols_gremio = gols
    gols_inter = int(gols_inter)
    gols_gremio = int(gols_gremio)

    jogos += 1

    if gols_inter > gols_gremio:
        vitorias["inter"] += 1
    elif gols_gremio > gols_inter:
        vitorias["gremio"] += 1
    else:
        vitorias["empates"] += 1

    mensagem = None

    if vitorias["gremio"] > vitorias["inter"]:
        mensagem = "Gremio venceu mais"
    elif vitorias["inter"] > vitorias["gremio"]:
        mensagem = "Inter venceu mais"
    else:
        mensagem = "Nao houve vencedor"

    opcao = None

    while opcao != 1 and opcao != 2:
        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input())

    if opcao == 2:
        print(f'{jogos} grenais')
        print(f'Inter:{vitorias["inter"]}')
        print(f'Gremio:{vitorias["gremio"]}')
        print(f'Empates:{vitorias["empates"]}')
        print(mensagem)
        break
