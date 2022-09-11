import os
import random
# Import da biblioteca de "random" para fazer as jogadas randômicas do computador.

pedra = 1   # Variáveis que representam as jogadas possíveis.
papel = 2
tesoura = 3

jogada1 = 0     # Variáveis utilizadas para comparar as jogadas.
jogada2 = 0

pontuacao1 = 0  # Variáveis que armazenam a pontuação para declarar o placar ao final de cada partida.
pontuacao2 = 0

jogador1 = "Computador 1"   # Variáveis que armazenam o nome dos jogadores ou dos computadores.
jogador2 = "Computador 2"   # Começa como "Computador 1" e "Computador 2" pois nos game modes 1 e 2 os jogadores colocam os próprios nomes, mas no 3 não precisa mudar nada.

continuarJogo = True    # Variável utilizada para continuar ou encerrar as partidas.

# Função que compara as jogadas utilizando as regras de Joquempo.
def comparar_jogadas():
    global pontuacao1
    global pontuacao2
    if jogada1 == pedra and jogada2 == tesoura:
        pontuacao1 += 1
        print(jogador1 + " venceu esta partida!")       # Utiliza as variáveis onde ficam os nomes dos jogadores para eles aparecerem na tela.

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

# Função utilizada para continuar ou encerrar as partidas.
def continuar_jogo():
    global continuarJogo

    print("Você quer continuar? \n"
          "1 - SIM \n"
          "2 - NÃO")

    continuarJogo = input("Continuar jogo? ")       # Input onde o jogador escolhe se quer continuar ou não a partida.

    if continuarJogo == "1":
        continuarJogo = True

    elif continuarJogo == "2":
        if pontuacao1 > pontuacao2:
            print(jogador1 + " venceu! Pontuação: " + str(pontuacao1))  # Print que mostra o nome do estudante e sua pontuação ao final da partida.
        elif pontuacao2 > pontuacao1:
            print(jogador2 + " venceu! Pontuação: " + str(pontuacao2))
        continuarJogo = False


    # Inicio do programa.
print("Bem vindo ao Joquempo! \n"
      "1 - Jogador x Jogador \n"
      "2 - Jogador x Computador \n"
      "3 - Computador x Computador")

gameMode = int(input("Selecione um modo de jogo: "))    # Variável utilizada para escolher o modo de jogo.

if gameMode == 1:

    jogador1 = input("Nome do jogador 1: ")     # Input que pede os nomes dos jogadores no inicio da partida.
    jogador2 = input("Nome do jogador 2: ")

    while continuarJogo:        # Enquanto "continuar jogo" for verdadeiro, a partida continua no mesmo modo de jogo.
        print("1 - PEDRA \n"
              "2 - PAPEL \n"
              "3 - TESOURA")

        jogada1 = int(input(jogador1 + " escreva qual sua jogada:  "))
        jogada2 = int(input(jogador2 + " escreva qual sua jogada:  "))

        comparar_jogadas()      # Chama a função que compara as jogadas e define o vencedor.
        continuar_jogo()        # Chama a função que pergunta se o jogador quer continuar o jogo.

if gameMode == 2:

    jogador1 = input("Nome do jogador: ")
    jogador2 = "Computador"     # Substitui o nome "Computador 2" armazenado na variável.

    while continuarJogo:

        print("1 - PEDRA \n"
              "2 - PAPEL \n"
              "3 - TESOURA")

        jogada1 = int(input(jogador1 + " escreva qual sua jogada:  "))
        jogada2 = random.randint(1, 3)                  # O computador escolhe um número aleatório entre 1 e 3.
        print(jogador2 + " jogou: " + str(jogada2))     # Print da jogada do computador.

        comparar_jogadas()
        continuar_jogo()

if gameMode == 3:

    while continuarJogo:         # Modo de jogo Computador vs Computador, portanto não pede inputs ao jogador.

        print("1 - PEDRA \n"
              "2 - PAPEL \n"
              "3 - TESOURA")

        jogada1 = random.randint(1, 3)
        print(jogador1 + " jogou: " + str(jogada1))
        jogada2 = random.randint(1, 3)
        print(jogador2 + " jogou: " + str(jogada2))

        comparar_jogadas()
        continuar_jogo()
