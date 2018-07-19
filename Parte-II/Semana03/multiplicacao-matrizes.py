def mat_mul(a, b):
    linhasA, colunasA = len(a), len(a[0])
    linhasB, colunasB = len(b), len(b[0])
    c = []

    for linha in range(linhasA):
        c.append([])
        for coluna in range(colunasB):
            c[linha].append(0)
            for k in range(colunasA):
                c[linha][coluna] += a[linha][k] * b[k][coluna]

    return c

if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
    print(mat_mul(a, b))
