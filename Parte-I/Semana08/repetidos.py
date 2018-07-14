def remove_repetidos(l):
    i = j = 0
    x = []
    while i < len(l):
        while j < len(l):
            if l[i] != l[j]:
                x.append(l[i])
            j += 1
        i += 1
    return x
