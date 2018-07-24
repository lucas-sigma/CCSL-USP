import pytest

def fatorialRec(n):
    return 1 if n == 0 else n * fatorial(n - 1)

def fatorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        fatorial = n
        while n > 1:
            n -= 1
            fatorial *= n
        return fatorial
        

#n = int(input("Digite o valor de n: "))
#print(fatorial(n))

@pytest.mark.parametrize('entrada, esperado', [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
