import os

pedra = 1
papel = 2
tesoura = 3

jogada1 = 0
jogada2 = 0

continuarJogo = True

while continuarJogo == True:

    print("Bem vindo ao Joquempo!")

    print("1 - PEDRA")
    print("2 - PAPEL")
    print("3 - TESOURA")

    jogada1 = int(input("Jogador 1 escreva qual sua jogada:  "))
    jogada2 = int(input("Jogador 2 escreva qual sua jogada:  "))

    if jogada1 == pedra and jogada2 == tesoura:
        print("Jogador 1 venceu")
    if jogada1 == tesoura and jogada2 == papel:
        print("Jogador 1 venceu")
    if jogada1 == papel and jogada2 == pedra:
        print("Jogador 1 venceu")

    if jogada1 == pedra and jogada2 == papel:
        print("Jogador 2 venceu")
    if jogada1 == papel and jogada2 == tesoura:
        print("Jogador 2 venceu")
    if jogada1 == tesoura and jogada2 == pedra:
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
        continuarJogo = False
