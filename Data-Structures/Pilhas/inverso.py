def main():

    seq = [11, 22, 33, 444]

    # Empilhar
    pilha = []
    for elemento in seq:
        pilha.append(elemento)

    # Desempilhar
    while len(pilha) > 0:
        print(pilha)
        topo = pilha.pop()
        print("objeto do topo: ", topo)

main()
