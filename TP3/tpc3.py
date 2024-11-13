#Solução do TPC3

import random

def computador_1(fosforos):
    jogada = (fosforos-1) % 5
    if jogada == 0:
        jogada = random.randint(1,4)
    print(f"O Computador retirou {jogada} fósforos.")
    return jogada

def jogador_1(fosforos):
    jogada = int(input("Escolha o número de fósforos que gostaria de tirar (1-4):"))
    if jogada in [1,2,3,4]:
        return jogada
    else:
        print("Jogada inválida. Tente novamente: escolha um número entre 1 e 4.")


def modo_jogador_1():
    fosforos = 21
    while fosforos > 0:
        jogada_jogador = jogador_1(fosforos)
        fosforos = fosforos - jogada_jogador
        if fosforos <= 0:
            print("Perdeste! O computador venceu.")
            return
        
        jogada_computador = computador_1(fosforos)
        fosforos = fosforos - jogada_computador
        if fosforos <= 0:
            print("O computador perdeu! Ganhaste o jogo!")
            return

def modo_computador_1():
    fosforos = 21
    while fosforos > 0:
        jogada_computador = computador_1(fosforos)
        fosforos = fosforos - jogada_computador
        if fosforos <= 0:
            print("O computador perdeu! Ganhaste o jogo!")
            return

        jogada_jogador = jogador_1(fosforos)
        fosforos = fosforos - jogada_jogador
        if fosforos <= 0:
            print("Perdeste! O computador venceu.")
            return


def comecar_jogo():
    print("Bem-vindo ao Jogo dos 21 Fósforos!")
    print("Começa por escolher o modo que queres jogar:")
    print("1 - O Jogador começa primeiro")
    print("2 - O Computador começa primeiro")

    cond = True
    
    while cond:
        escolha = input("Escolhe o modo de jogo (1 ou 2): ")
        
        if escolha == "1":
            modo_jogador_1()
            cond = False
        elif escolha == "2":
            modo_computador_1()
            cond = False
        else:
            print("Escolha inválida. Por favor, escolhe 1 ou 2.")


comecar_jogo()
