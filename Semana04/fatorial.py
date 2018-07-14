def fatorialRec(n):
    return 1 if n == 0 else n * fatorial(n - 1)

def fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = n
        while n > 1:
            n -= 1
            fatorial *= n
        return fatorial
        

n = int(input("Digite o valor de n: "))
print(fatorial(n))
