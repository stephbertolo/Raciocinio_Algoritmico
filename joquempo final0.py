import os
import random
from re import I
'''joquempo'''
pedra = 1
papel = 2
tesoura = 3

jogada1_vs_jogada2 = 1
jogada1_vs_computador1 = 2
computador1_vs_computador2 = 3

jogada1 = 0
jogada2 = 0

computador1 = 0
computador2 = 0

score1 = 0 #Pontuação do jogador/computador 1
score2 = 0 #Pontuação do jogador/computador 2

continuarJogo = True

print("Bem-vindo ao Joquempô!") #Mensagens inicial do jogo de boas-vindas

print("Modos de jogo: ") #O jogo possui três opções de modo de jogo que serão escolhidas se acordo com o número digitado pelo jogador.
print("1 = jogador vs jogador")
print("2 = jogador vs computador")
print("3 = computador vs computador")
modo_de_jogo = int(input("Com qual modo de jogo você deseja jogar? "))

while modo_de_jogo == jogada1_vs_jogada2 and continuarJogo: #Esse modo de jogo é jogado por pessoaXpessoa, logo os dois valores precisam ser informados.
     print("1 - PEDRA")
     print("2 - PAPEL")
     print("3 - TESOURA")

     jogada1 = int(input("Jogador 1 escreva qual a sua jogada:  "))
     jogada2 = int(input("Jogador 2 escreva qual a sua jogada:  "))

     if jogada1 == pedra and jogada2 == tesoura:
        score1 += 1 # A pontuação é mostrada a cada partida e os valores são acumulados para serem mostrados novamente ao final do jogo inidicando o vencedor final.
        print("Jogador 1 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == tesoura and jogada2 == papel:
        score1 += 1
        print("Jogador 1 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == papel and jogada2 == pedra:
        score1 += 1
        print("Jogador 1 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))

     elif jogada1 == pedra and jogada2 == papel:
        score2 += 1
        print("Jogador 2 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == papel and jogada2 == tesoura:
        score2 += 1
        print("Jogador 2 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == tesoura and jogada2 == pedra:
        score2 += 1
        print("Jogador 2 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))

     else : #Em caso de empate, nenhum dos dois jogadores acumulam pontos.
        print("Empate!")
        print(str(score1) + " X " + str(score2))        

     print("Você deseja continuar jogando?")
     print("1 - SIM")
     print("2 - NÃO")
     continuarJogo = input("Continuar jogo? ")

     if continuarJogo == "1":
        continuarJogo = True
     elif continuarJogo == "2":#O jogo encera informando quem foi o jogador final de acordo com a pontuação acumulada.
        if score1 > score2:
            print("Jogador 1 é o vencedor final do jogo!")
        elif score1 < score2:
            print("Jogador 2 é o vencedor final do jogo!")
        else:
            print("Os jogadores empataram o jogo!")
        print("PLACAR GERAL")
        print("Jogador 1: " + str(score1))
        print("Jogador 2: " + str(score2))
        print("Obrigado por jogar! :)")
        print("Melyça\ne\nSthefany\nDisciplina de Raciocínio Algorítmico - Professora Marina de Lara Muller") #3ASCII LF line feed; quebra linha
        continuarJogo = False



while modo_de_jogo == jogada1_vs_computador1 and continuarJogo:#Nesse modo de jogo um dos valores será informado pelo jogador(humano) e o outro será gerado de forma aleatória pelo programa.
     
     jogada1 = int(input("Jogador 1 escreva qual a sua jogada:  "))
     computador1 = random.randint(1, 3) #randint gera aleatóriamnete um número inteiro dentro do intevalo de 1 a 3 (incluindo o 3)
     print("Jogada do computador:" + str(computador1)) #"print" para ficar visível o número fornecido na função randint.

     if jogada1 == pedra and computador1 == tesoura:
        score1 += 1
        print("Jogador 1 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == tesoura and computador1 == papel:
        score1 += 1
        print("Jogador 1 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == papel and computador1 == pedra:
        score1 += 1
        print("Jogador 1 é o vencedor da partida.")
        print(str(score1) + " X " + str(score2))

     elif jogada1 == pedra and computador1 == papel:
        score2 += 1
        print("O Computador venceu a partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == papel and computador1 == tesoura:
        score2 += 1
        print("O Computador venceu a partida.")
        print(str(score1) + " X " + str(score2))
     elif jogada1 == tesoura and computador1 == pedra:
        score2 += 1
        print("O Computador venceu a partida.")
        print(str(score1) + " X " + str(score2))

     else : #Sem pontos, para ambos, quando ocorre empate.
        print("Empate!")
        print(str(score1) + " X " + str(score2))

     print("Você quer continuar?")
     print("1 - SIM")
     print("2 - NÃO")
     continuarJogo = input("Continuar jogo? ")

     if continuarJogo == "1":
        continuarJogo = True
     elif continuarJogo == "2":
        continuarJogo = True
        if score1 > score2:
            print("Jogador 1 é o vencedor final do jogo!")
        elif score1 < score2:
            print("O computador é o vencedor final do jogo!")
        else:
            print("Os jogadores empataram o jogo!")
        print("PLACAR GERAL")
        print("Jogador 1: " + str(score1))
        print("Computador: " + str(score2))
        print("Obrigado por jogar! :)")
        print("Melyça\ne\nSthefany\nDisciplina de Raciocínio Algorítmico - Professora Marina de Lara Muller") #3ASCII LF line feed; quebra linha
        continuarJogo = False 

while modo_de_jogo == computador1_vs_computador2 and continuarJogo: #Modo de jogo em que os dois valores serão gerados aleatoriamente.
     
     computador1 = random.randint(1, 3)
     computador2 = random.randint(1, 3)
     print("Jogada do Computador 1:  " + str(computador1))
     print("Jogada do Computador 2:  " + str(computador2))

     if computador1 == pedra and computador2 == tesoura:
        score1 += 1
        print("O Computador 1 venceu a partida.")
        print(str(score1) + " X " + str(score2))
     elif computador1 == tesoura and computador2 == papel:
        score1 += 1
        print("O Computador 1 venceu a partida.")
        print(str(score1) + " X " + str(score2))
     elif computador1 == papel and computador2 == pedra:
        score1 += 1
        print("O Computador 1 venceu a partida.")
        print(str(score1) + " X " + str(score2))

     elif computador1 == pedra and computador2 == papel:
        score2 += 1
        print("O Computador 2 venceu a partida.")
        print(str(score1) + " X " + str(score2))
     elif computador1 == papel and computador2 == tesoura:
        score2 += 1
        print("O Computador 2 venceu a partida.")
        print(str(score1) + " X " + str(score2))
     elif computador1 == tesoura and computador2 == pedra:
        score2 += 1
        print("O Computador 2 venceu a partida.")
        print(str(score1) + " X " + str(score2))
    
     else :#Sem pontos, para ambos, quando ocorre empate.
        print("Empate!")
        print(str(score1) + " X " + str(score2))

     print("Você desejar continuar o jogo?")
     print("1 - SIM")
     print("2 - NÃO")
     continuarJogo = input("Continuar jogo? ")

     if continuarJogo == "1":
        continuarJogo = True
     elif continuarJogo == "2":
        continuarJogo = False
        if score1 > score2:
            print("Computador 1 é o vencedor final do jogo!")
        elif score1 < score2:
            print("Computador 2 é o vencedor final do jogo!")
        else:
            print("Os jogadores empataram o jogo!")
        print("PLACAR GERAL")
        print("Computador 1:  " + str(score1))
        print("Computador 2:  " + str(score2))
        print("Obrigado por jogar! :)")
        print("Melyça\ne\nSthefany\nDisciplina de Raciocínio Algorítmico - Professora Marina de Lara Muller") #3ASCII LF line feed; quebra linha
        continuarJogo = False #Fim do código.