n = int(input("Digite um número inteiro: "))

def soma(n):
    adjacentes = 0
    while n > 0:
        x = n % 10
        n //= 10
        adjacentes += x
    return adjacentes

print(soma(n))
