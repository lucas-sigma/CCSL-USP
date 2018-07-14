x = n = int(input("Digite o valor de n: "))
adj = 0

while n > 0:
    x %= 10
    n //= 10
    if x == (n % 10):
        print("sim")
        adj = 1
        n = 0
    x = n % 10

if adj == 0:
    print("não")
