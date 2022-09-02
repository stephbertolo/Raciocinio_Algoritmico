import os
import random

pedra = 1
papel = 2
tesoura = 3

jogada1 = 0
jogada2 = 0

pontuacao1 = 0
pontuacao2 = 0

gameMode = 0

continuarJogo = True

print("Bem vindo ao Joquempo!")

print("1 - Jogador x Jogador")
print("2 - Jogador x Computador")
print("3 - Computador x Computador")

gameMode = int(input("Selecione um modo de jogo: "))

if gameMode == 1:

    while continuarJogo == True:

        print("1 - PEDRA")
        print("2 - PAPEL")
        print("3 - TESOURA")

        jogada1 = int(input("Jogador 1 escreva qual sua jogada:  "))
        jogada2 = int(input("Jogador 2 escreva qual sua jogada:  "))

        if jogada1 == pedra and jogada2 == tesoura:
            pontuacao1 += 1
            print("Jogador 1 venceu")
        if jogada1 == tesoura and jogada2 == papel:
            pontuacao1 += 1
            print("Jogador 1 venceu")
        if jogada1 == papel and jogada2 == pedra:
            pontuacao1 += 1
            print("Jogador 1 venceu")

        if jogada1 == pedra and jogada2 == papel:
            pontuacao2 += 1
            print("Jogador 2 venceu")
        if jogada1 == papel and jogada2 == tesoura:
            pontuacao2 += 1
            print("Jogador 2 venceu")
        if jogada1 == tesoura and jogada2 == pedra:
            pontuacao2 += 1
            print("Jogador 2 venceu")

        if jogada1 == jogada2:
            print("Empate")


        print("Você quer continuar?")
        print("1 - SIM")
        print("2 - NÃO")
        continuarJogo = input("Continuar jogo? ")

        if continuarJogo == "1":
            continuarJogo = True

        if continuarJogo == "2":
            if pontuacao1 > pontuacao2:
                print("Jogador 1 venceu! Pontuação: " + str(pontuacao1))
            if pontuacao2 > pontuacao1:
                print("Jogador 2 venceu! Pontuação: " + str(pontuacao2))
            continuarJogo = False

if gameMode == 2:

    while continuarJogo == True:

        print("1 - PEDRA")
        print("2 - PAPEL")
        print("3 - TESOURA")

        jogada1 = int(input("Jogador 1 escreva qual sua jogada:  "))
        jogada2 = random.randint(1, 3)
        print("Computador jogou: " + str(jogada2))

        if jogada1 == pedra and jogada2 == tesoura:
            pontuacao1 += 1
            print("Jogador 1 venceu")
        if jogada1 == tesoura and jogada2 == papel:
            pontuacao1 += 1
            print("Jogador 1 venceu")
        if jogada1 == papel and jogada2 == pedra:
            pontuacao1 += 1
            print("Jogador 1 venceu")

        if jogada1 == pedra and jogada2 == papel:
            pontuacao2 += 1
            print("Computador venceu")
        if jogada1 == papel and jogada2 == tesoura:
            pontuacao2 += 1
            print("Computador venceu")
        if jogada1 == tesoura and jogada2 == pedra:
            pontuacao2 += 1
            print("Computador venceu")

        if jogada1 == jogada2:
            print("Empate")

        print("Você quer continuar?")
        print("1 - SIM")
        print("2 - NÃO")
        continuarJogo = input("Continuar jogo? ")

        if continuarJogo == "1":
           continuarJogo = True

        if continuarJogo == "2":
           if pontuacao1 > pontuacao2:
              print("Jogador 1 venceu! Pontuação: " + str(pontuacao1))
           if pontuacao2 > pontuacao1:
                print("Computador venceu! Pontuação: " + str(pontuacao2))
           continuarJogo = False