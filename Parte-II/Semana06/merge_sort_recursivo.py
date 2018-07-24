def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    return direita if not esquerda else esquerda if not direita else [esquerda[0]] + merge(esquerda[1:], direita) if esquerda[0] < direita[0] else [direita[0]] + merge(esquerda, direita[1:])
