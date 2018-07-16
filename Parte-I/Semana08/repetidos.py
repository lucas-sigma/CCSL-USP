def remove_repetidos(l):
    x = l[:]  # lista auxiliar

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                x[j] = ' '
                
    for i in range(len(l)):
        if ' ' in x: x.remove(' ')

    return sorted(x)
