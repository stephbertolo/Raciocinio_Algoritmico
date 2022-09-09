import os
import random

pedra = 1
papel = 2
tesoura = 3

jogada1 = 0
jogada2 = 0

pontuacao1 = 0
pontuacao2 = 0

jogador1 = "Computador 1"
jogador2 = "Computador 2"

continuarJogo = True


def comparar_jogadas():
    global pontuacao1
    global pontuacao2

    if jogada1 == pedra and jogada2 == tesoura:
        pontuacao1 += 1
        print(jogador1 + " venceu esta partida!")

    elif jogada1 == tesoura and jogada2 == papel:
        pontuacao1 += 1
        print(jogador1 + " venceu esta partida!")
    elif jogada1 == papel and jogada2 == pedra:
        pontuacao1 += 1
        print(jogador1 + " venceu esta partida!")

    elif jogada1 == pedra and jogada2 == papel:
        pontuacao2 += 1
        print(jogador2 + " venceu esta partida!")
    elif jogada1 == papel and jogada2 == tesoura:
        pontuacao2 += 1
        print(jogador2 + " venceu esta partida!")
    elif jogada1 == tesoura and jogada2 == pedra:
        pontuacao2 += 1
        print(jogador2 + " venceu esta partida!")
    else:
        print("Empate")


def continuar_jogo():
    global continuarJogo

    print("Você quer continuar? \n"
          "1 - SIM \n"
          "2 - NÃO")

    continuarJogo = input("Continuar jogo? ")

    if continuarJogo == "1":
        continuarJogo = True

    elif continuarJogo == "2":
        if pontuacao1 > pontuacao2:
            print(jogador1 + " venceu! Pontuação: " + str(pontuacao1))
        elif pontuacao2 > pontuacao1:
            print(jogador2 + " venceu! Pontuação: " + str(pontuacao2))
        continuarJogo = False


print("Bem vindo ao Joquempo! \n"
      "1 - Jogador x Jogador \n"
      "2 - Jogador x Computador \n"
      "3 - Computador x Computador")

gameMode = int(input("Selecione um modo de jogo: "))

if gameMode == 1:

    jogador1 = input("Nome do jogador 1: ")
    jogador2 = input("Nome do jogador 2: ")

    while continuarJogo:
        print("1 - PEDRA \n"
              "2 - PAPEL \n"
              "3 - TESOURA")

        jogada1 = int(input(jogador1 + " escreva qual sua jogada:  "))
        jogada2 = int(input(jogador2 + " escreva qual sua jogada:  "))

        comparar_jogadas()
        continuar_jogo()

if gameMode == 2:

    jogador1 = input("Nome do jogador: ")
    jogador2 = "Computador"

    while continuarJogo:

        print("1 - PEDRA \n"
              "2 - PAPEL \n"
              "3 - TESOURA")

        jogada1 = int(input(jogador1 + " escreva qual sua jogada:  "))
        jogada2 = random.randint(1, 3)
        print(jogador2 + " jogou: " + str(jogada2))

        comparar_jogadas()
        continuar_jogo()

if gameMode == 3:

    while continuarJogo:

        print("1 - PEDRA \n"
              "2 - PAPEL \n"
              "3 - TESOURA")

        jogada1 = random.randint(1, 3)
        print(jogador1 + " jogou: " + str(jogada1))
        jogada2 = random.randint(1, 3)
        print(jogador2 + " jogou: " + str(jogada2))

        comparar_jogadas()
        continuar_jogo()
