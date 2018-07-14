def maior_primo(n):
    tot = a = b = 0
    i = 2
    j = 1
    while i <= n:
        while j <= n:
            if i % j == 0:
                tot += 1
            j += 1
        if tot == 2:
            a = i
        i += 1
        j = 1
        tot = 0
    return a
