def computador_escolhe_jogada(n, m):
    if m >= n:
        print("Computador pegou ", n, " peças")
        return n
    else:
        x = n % (m + 1)
        if x > 0:
            print("Computador pegou ", x, " peças")
            return x
        print("Computador pegou ", m, " peças")
        return m

def usuario_escolhe_jogada(n, m):
    j = int(input("Informe sua jogada"))
    while j > m or j < 1 or j > n: 
        print("Jogada inválida. Tente novamente")
        j = int(input("Informe sua jogada"))
    print("Jogador pegou ", j, " peças")
    return j

def partida():    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print("Você começa!")
        while n > 0:
            if n > 0:
                j = usuario_escolhe_jogada(n, m)
                n = n - j
                print("Agora restam ", n, " peças no tabuleiro.")
                if n == 0:
                    print("Fim de jogo. Você venceu!")
            if n > 0:
                j = computador_escolhe_jogada(n, m)
                n = n - j
                print("Agora restam ", n, " peças no tabuleiro.")
                if n == 0:
                    print("Fim de jogo. Computador venceu!")
    else:
        print("Computador começa!")
        while n > 0:
            if n > 0:
                j = computador_escolhe_jogada(n, m)
                n = n - j
                print("Agora restam ", n, " peças no tabuleiro.")
                if n == 0:
                    print("Fim de jogo. Computador venceu!")
            if n > 0:
                j = usuario_escolhe_jogada(n, m)
                n = n - j
                print("Agora restam ", n, " peças no tabuleiro.")
                if n == 0:
                    print("Fim de jogo. Você venceu!")

def campeonato():
    for i in range(1, 4):
        print("**** Rodada ", i, " ****")
        partida()
    print("**** Final do campeonato! ****")
    print("\nPlacar: Você 0", " X ", i, " Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("\n1 - para jogar uma partida isolada")
escolha = int(input("2 - para jogar um campeonato\n"))

if escolha == 1:
    partida()
elif escolha == 2:
    campeonato()
