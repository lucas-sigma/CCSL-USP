def mais_curto(l):
    y = l[0]
    for i in range(len(l)):
        if l[i] < y:
            y = l[i]
    return y
