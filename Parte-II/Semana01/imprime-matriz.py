def imprime_matriz(m):
    if len(m) == 1:
        return m[0][0]
    else:
        for i in range(len(m)):
            for j in range(len(m) + 1):
                print(m[i][j], end=" ")
            print()
