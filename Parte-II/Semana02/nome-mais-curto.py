def mais_curto(l):
    y = l[0].strip()
    for i in range(len(l)):
        if len(l[i].strip()) < len(y):
            y = l[i].strip()
    return y.capitalize()
