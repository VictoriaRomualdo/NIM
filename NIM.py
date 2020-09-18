def computador_escolhe_jogada(n, m):
    resto = n % (m + 1)

    if resto == 0:
        return m
    else:
        return resto


def usuario_escolhe_jogada(n, m):
    valida = 0

    while not valida:
        jogada = int(input("Digite o número de peças que serão removidas: "))
        if 0 < jogada <= m:
            valida = 1
        else:
            print("Jogada Inválida, tente novamente!")
    return jogada


def partida():
    n = 0
    m = 0
    jogador = 0  # pc vai ser 1 e 2 usuario
    while n <= 0:
        n = int(input("Digite o número total de peças iniciais: "))
    while m <= 0 or m > n:
        m = int(input("Digite o número máximo de peças que o jogador pode retirar por jogada, não pode ser zero: "))

    resto = n % (m + 1)

    if resto == 0:
        print("Você começa!")
        jogador = 2
    else:
        print("Computador começa!")
        jogador = 1

    while n > 0:
        if jogador == 1:
            print("Vez do computador")
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            jogador = 2
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            jogador = 1
        print("Foram removidas {} peças. Restam {} peças no tabuleiro.".format(jogada, n))

    print("Jogo encerrado!")
    print("O computador ganhou!")


def campeonato():
    rodada = 1

    while rodada <= 3:
        print("**** Rodada {} ****".format(rodada))
        partida()
        rodada = rodada + 1
    print("Final de campeonato!")
    print("Computador venceu!")
    print(" ")
    print("Placar: Você 0 X 3 Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print(" ")
print("1 - para jogar uma partida isolada ")
opcao = int(input("2 - para jogar um campeonato "))
print(" ")

if (opcao == 1):
    print("Voce escolheu partida isolada!")
    partida()
if (opcao == 2):
    print("Voce escolheu um campeonato!")
    campeonato()