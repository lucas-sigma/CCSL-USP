def primo(n):
    fator = 2
    if n == 2:
        return True

    while n % fator != 0 and fator <= n/2:
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True

def limite():
    lista = []
    limite = int(input("Digite um limite máximo: "))
    n = 2   # Primeiro primo.
    while n < limite:
        if primo(n):
            lista.append(n)
            #print(n, end=', ')
        n += 1
    print(lista)
limite()