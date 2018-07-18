def dimensoes(m):
    i = 0
    for each in range(len(m)):
        j = 0
        for nested in range(len(m[each])):
            j += 1
        i += 1
    return i, ' X ', j

def soma_matrizes(m1, m2):
    soma = m1[:]
    if dimensoes(m1) == dimensoes(m2):
        if len(m1) == 1:
            soma[0][0] = m1[0][0] + m2[0][0]
            return soma
        else:
            for i in range(len(m1)):
                for j in range(len(m1)):
                    soma[i][j] = m1[i][j] + m2[i][j]
            soma[-1][-1] = m1[-1][-1] + m2[-1][-1]
            soma[0][-1] = m1[0][-1] + m2[0][-1]
            return soma
    return False
